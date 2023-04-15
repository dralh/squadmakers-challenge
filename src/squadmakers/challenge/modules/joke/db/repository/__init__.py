from .abc import JokeRepository
from .chuck_repository import ChuckJokeRepository
from .dad_repository import DadJokeRepository
from .postgres_repository import PostgresJokeRepository

__all__ = [
    "JokeRepository",
    "ChuckJokeRepository",
    "DadJokeRepository",
    "PostgresJokeRepository",
]
