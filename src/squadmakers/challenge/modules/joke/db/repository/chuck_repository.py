from typing import Optional
from urllib.parse import urljoin

import requests

from squadmakers.challenge.modules.joke.db.repository.abc import JokeRepository
from squadmakers.challenge.modules.joke.model import Joke

API_URL = "https://api.chucknorris.io"


class ChuckJokeRepository(JokeRepository):
    def get_random_joke(self) -> Joke:
        res = requests.get(urljoin(API_URL, "/jokes/random"))
        try:
            res.raise_for_status()
            body = res.json()
        except requests.exceptions.HTTPError:
            raise RuntimeError("No joke :(")

        joke = Joke()
        joke.joke_id = None
        joke.content = body.get("value")
        return joke

    def get_joke_by_id(self, joke_id: int) -> Optional[Joke]:
        raise NotImplementedError

    def delete_joke(self, joke: Joke) -> None:
        raise NotImplementedError

    def save_joke(self, joke: Joke) -> None:
        raise NotImplementedError
