from werkzeug.exceptions import BadRequest

__all__ = ["InvalidNumberException"]


class InvalidNumberException(BadRequest):
    pass
