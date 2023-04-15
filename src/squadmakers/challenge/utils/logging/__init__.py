from logging import getLogger
from logging.config import dictConfig

__all__ = ["setup_logging"]


def setup_logging(config: dict):
    if config:
        dictConfig(config)
    else:
        getLogger(__name__).warning("No logging config was provided.")
