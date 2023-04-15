from logging import getLogger

import arrow
from flask import Response, jsonify, make_response
from werkzeug.exceptions import HTTPException

__all__ = ["handle_http_exception"]


def handle_http_exception(exc: HTTPException) -> Response:
    return make_response(
        jsonify(
            name=exc.__class__.__qualname__,
            message=exc.description,
            timestamp=arrow.utcnow().format(),
        ),
        exc.code,
    )


def handle_any_error(exc: Exception):
    getLogger(__name__).exception(
        f'Unhandled "{type(exc).__module__}.{type(exc).__qualname__}".'
    )
    return make_response(
        jsonify(
            error=type(exc).__qualname__,
            message=str(exc),
            timestamp=arrow.utcnow().for_json(),
            status=500,
        ),
        500,
    )
