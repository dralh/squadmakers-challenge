from werkzeug.exceptions import NotFound

__all__ = ["JokeNotFoundException"]


class JokeNotFoundException(NotFound):
    pass
