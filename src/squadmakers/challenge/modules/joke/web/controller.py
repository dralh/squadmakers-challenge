import random

from flask import Blueprint, jsonify, request

from squadmakers.challenge.modules.joke.db.repository import (
    ChuckJokeRepository,
    DadJokeRepository,
    PostgresJokeRepository,
)
from squadmakers.challenge.modules.joke.model.joke_provider import JokeProvider
from squadmakers.challenge.modules.joke.use_case import JokeUseCase

__all__ = ["joke_blueprint"]


joke_blueprint = Blueprint("joke", __name__, url_prefix="/joke")


@joke_blueprint.route("", methods=["GET"])
def get_random_joke():
    repository_cls = random.choice([ChuckJokeRepository, DadJokeRepository])
    joke = JokeUseCase(repository=repository_cls()).get_random_joke()
    return jsonify(joke)


@joke_blueprint.route("<string:joke_provider>", methods=["GET"])
def get_random_joke_by_provider(joke_provider: str):
    if joke_provider.upper() == JokeProvider.CHUCK.name:
        repository = ChuckJokeRepository()
    elif joke_provider.upper() == JokeProvider.DAD.name:
        repository = DadJokeRepository()
    else:
        raise RuntimeError("Invalid joke provider")

    joke = JokeUseCase(repository=repository).get_random_joke()
    return jsonify(joke)


@joke_blueprint.route("/", methods=["POST"])
def create_joke():
    body = request.get_json()
    joke = JokeUseCase(repository=PostgresJokeRepository()).create_joke(
        content=body.get("content")
    )
    return jsonify(joke)


@joke_blueprint.route("/<int:number>", methods=["PUT"])
def edit_joke(number: int):
    body = request.get_json()
    joke = JokeUseCase(repository=PostgresJokeRepository()).edit_joke(
        joke_id=number,
        content=body.get("content"),
    )
    return jsonify(joke)


@joke_blueprint.route("<int:number>", methods=["DELETE"])
def delete_joke(number: int):
    JokeUseCase(repository=PostgresJokeRepository()).delete_joke(
        joke_id=number,
    )
    return jsonify()
