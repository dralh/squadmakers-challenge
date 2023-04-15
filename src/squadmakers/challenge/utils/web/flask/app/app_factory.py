from http import HTTPStatus
from logging import getLogger
from typing import List

from flask import Blueprint, Flask, jsonify, make_response
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import HTTPException
from werkzeug.middleware.proxy_fix import ProxyFix

from squadmakers.challenge.utils.web.flask.exc.handler import (
    handle_http_exception,
)

__all__ = ["AppFactory"]


class AppFactory:
    blueprints: List[Blueprint]
    _version: str
    _scoped_session: scoped_session

    def __init__(self, version: str, scoped_session_: scoped_session = None):
        self.blueprints = []
        self._version = version
        self._scoped_session = scoped_session_

    def register_blueprint(self, blueprint: Blueprint) -> None:
        self.blueprints.append(blueprint)

    def make_flask(self, config: dict = None) -> Flask:
        """
        Flask application factory function.

        :param config: Config dict.
        :return: Initialized Flask application.
        """
        app = self._create_app(config)

        # Add ProxyFix middleware if needed.
        if app.config.get("REVERSE_PROXY", False):
            app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)
            getLogger(__name__).info("Accepting reverse proxy headers.")

        return app

    def _create_app(self, config: dict = None) -> Flask:
        """
        Application factory function.
        Based on https://flask.palletsprojects.com/en/latest/patterns/appfactories/

        :param config: Config dict
        :return: Initialized Flask application
        """
        app = Flask(__name__)

        if config:
            app.config.update(config)
            getLogger(__name__).info("Loaded config " + str(config))

        # Register blueprints
        for b in self.blueprints:
            app.register_blueprint(b)

        # Register error handlers
        app.register_error_handler(HTTPException, handle_http_exception)

        @app.teardown_appcontext
        def cleanup(resp_or_exc):
            if self._scoped_session:
                self._scoped_session.remove()

        # Metadata endpoint
        @app.route("/")
        def metadata():
            return make_response(jsonify(version=self._version), HTTPStatus.OK)

        # Heartbeat endpoint
        @app.route("/heartbeat")
        def heartbeat():
            return make_response(jsonify(status="alive"), HTTPStatus.OK)

        return app
