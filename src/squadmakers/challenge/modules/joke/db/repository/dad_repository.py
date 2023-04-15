from typing import Optional

import requests

from squadmakers.challenge.modules.joke.db.repository.abc import JokeRepository
from squadmakers.challenge.modules.joke.model import Joke

API_URL = "https://icanhazdadjoke.com/"


__all__ = ["DadJokeRepository"]


class DadJokeRepository(JokeRepository):
    def get_random_joke(self) -> Joke:
        headers = {"Accept": "application/json"}
        res = requests.get(API_URL, headers=headers)
        try:
            res.raise_for_status()
            body = res.json()
        except requests.exceptions.HTTPError:
            raise RuntimeError("No joke :(")

        joke = Joke()
        joke.joke_id = None
        joke.content = body.get("joke")
        return joke

    def get_joke_by_id(self, joke_id: int) -> Optional[Joke]:
        raise NotImplementedError

    def delete_joke(self, joke: Joke) -> None:
        raise NotImplementedError

    def save_joke(self, joke: Joke) -> None:
        raise NotImplementedError
