from squadmakers.challenge import __version__
from squadmakers.challenge.config import config
from squadmakers.challenge.database.sqlalchemy import Session
from squadmakers.challenge.modules.joke.web.controller import joke_blueprint
from squadmakers.challenge.utils.web.flask.app.app_factory import AppFactory

app_factory = AppFactory(__version__, Session)
app_factory.register_blueprint(joke_blueprint)

app = app_factory.make_flask(config)
