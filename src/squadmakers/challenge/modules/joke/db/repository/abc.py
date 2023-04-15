from abc import ABC, abstractmethod
from typing import Optional

__all__ = ["JokeRepository"]

from squadmakers.challenge.modules.joke.model import Joke


class JokeRepository(ABC):
    @abstractmethod
    def get_random_joke(self) -> Joke:
        pass

    @abstractmethod
    def get_joke_by_id(self, joke_id: int) -> Optional[Joke]:
        pass

    @abstractmethod
    def delete_joke(self, joke: Joke) -> None:
        pass

    @abstractmethod
    def save_joke(self, joke: Joke) -> None:
        pass
