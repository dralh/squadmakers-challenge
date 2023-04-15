import arrow
from flask import Response, jsonify, make_response
from werkzeug.exceptions import (
    BadRequest,
    Forbidden,
    HTTPException,
    InternalServerError,
    NotFound,
    TooManyRequests,
    Unauthorized,
)

__all__ = ["handle_http_exception"]


def handle_http_exception(exc: HTTPException) -> Response:
    exception_name = InternalServerError.name

    # 400
    if isinstance(exc, BadRequest):
        exception_name = BadRequest.name
    # 401
    if isinstance(exc, Unauthorized):
        exception_name = Unauthorized.name
    # 403
    if isinstance(exc, Forbidden):
        exception_name = Forbidden.name
    # 404
    if isinstance(exc, NotFound):
        exception_name = NotFound.name
    # 429
    if isinstance(exc, TooManyRequests):
        exception_name = TooManyRequests.name

    return make_response(
        jsonify(
            name=exception_name,
            message=exc.description,
            timestamp=arrow.utcnow(),
        ),
        exc.code,
    )
