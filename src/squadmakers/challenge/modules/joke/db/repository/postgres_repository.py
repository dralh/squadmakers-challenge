from typing import Optional

from squadmakers.challenge.database.sqlalchemy import Session, mapper_registry
from squadmakers.challenge.modules.joke.db.entity.joke_entity import joke_table
from squadmakers.challenge.modules.joke.model import Joke

from .abc import JokeRepository

mapper_registry.map_imperatively(Joke, joke_table)


class PostgresJokeRepository(JokeRepository):
    def get_random_joke(self) -> Joke:
        raise NotImplemented

    def get_joke_by_id(self, joke_id: int) -> Optional[Joke]:
        session = Session()
        joke = session.query(Joke).filter_by(joke_id=joke_id).one_or_none()
        return joke

    def delete_joke(self, joke: Joke) -> None:
        session = Session()
        session.delete(joke)
        session.commit()

    def save_joke(self, joke: Joke) -> None:
        session = Session()
        session.add(joke)
        session.commit()
