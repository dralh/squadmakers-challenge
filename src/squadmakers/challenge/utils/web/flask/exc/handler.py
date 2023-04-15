from logging import getLogger

import arrow
from flask import Response, jsonify, make_response
from werkzeug.exceptions import (
    BadRequest,
    Forbidden,
    HTTPException,
    NotFound,
    TooManyRequests,
    Unauthorized,
)

__all__ = ["handle_http_exception"]


def handle_http_exception(exc: HTTPException) -> Response:
    exception_name = "InternalServerError"

    # 400
    if isinstance(exc, BadRequest):
        exception_name = "BadRequest"
    # 401
    if isinstance(exc, Unauthorized):
        exception_name = "Unauthorized"
    # 403
    if isinstance(exc, Forbidden):
        exception_name = "Forbidden"
    # 404
    if isinstance(exc, NotFound):
        exception_name = "NotFound"
    # 429
    if isinstance(exc, TooManyRequests):
        exception_name = "TooManyRequests"

    return make_response(
        jsonify(
            name=exception_name,
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
