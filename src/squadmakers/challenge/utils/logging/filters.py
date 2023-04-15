"""
Custom logging filters.

Provides convenience Python logging filters.
"""

import logging
from logging import Filter

__all__ = ["LevelFilter"]


class LevelFilter(Filter):
    """
    Filters logging records above a certain log level.
    """

    def __init__(self, level: str):
        """
        Initialize a LevelFilter.
        :param level: Maximum log level to allow through.
        """
        super().__init__()
        self._level = getattr(logging, level)

    def filter(self, record):
        return record.levelno <= self._level
