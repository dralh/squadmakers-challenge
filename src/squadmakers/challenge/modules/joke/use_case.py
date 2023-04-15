from squadmakers.challenge.modules.joke.db.repository import JokeRepository
from squadmakers.challenge.modules.joke.model import Joke

__all__ = ["JokeUseCase"]


class JokeUseCase:
    repository: JokeRepository

    def __init__(self, repository=None):
        self.repository = repository

    def get_random_joke(self) -> Joke:
        joke = self.repository.get_random_joke()
        return joke

    def get_joke_by_id(self, joke_id: int) -> Joke:
        joke = self.repository.get_joke_by_id(joke_id)

        if not joke:
            raise RuntimeError("Joke not found")

        return joke

    def create_joke(self, content: str) -> Joke:
        joke = Joke()
        joke.content = content
        self.repository.save_joke(joke)
        return joke

    def edit_joke(self, joke_id: int, content: str) -> Joke:
        joke = self.repository.get_joke_by_id(joke_id)

        if not joke:
            raise RuntimeError("Joke not found")

        joke.content = content
        self.repository.save_joke(joke)
        return joke

    def delete_joke(self, joke_id: int) -> None:
        joke = self.repository.get_joke_by_id(joke_id)

        if not joke:
            raise RuntimeError("Joke not found")

        self.repository.delete_joke(joke)
