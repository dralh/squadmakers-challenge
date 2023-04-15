from typing import Optional

from squadmakers.challenge.modules.joke.db.repository import JokeRepository
from squadmakers.challenge.modules.joke.model import Joke


class SuccessfulFakeRepository(JokeRepository):
    def get_random_joke(self) -> Joke:
        joke = Joke()
        joke.joke_id = None
        joke.content = "a basic joke"
        return joke

    def get_joke_by_id(self, joke_id: int) -> Optional[Joke]:
        joke = Joke()
        joke.joke_id = joke_id
        joke.content = "a basic joke"
        return joke

    def delete_joke(self, joke: Joke) -> None:
        pass

    def save_joke(self, joke: Joke) -> None:
        joke.joke_id = 1


class NotFoundFakeRepository(JokeRepository):
    def get_random_joke(self) -> Joke:
        raise RuntimeError

    def get_joke_by_id(self, joke_id: int) -> Optional[Joke]:
        return

    def delete_joke(self, joke: Joke) -> None:
        pass

    def save_joke(self, joke: Joke) -> None:
        pass
