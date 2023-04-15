import pytest

from squadmakers.challenge.modules.joke.use_case import JokeUseCase

from .fake_repository import NotFoundFakeRepository, SuccessfulFakeRepository


def test_get_random_joke():
    repository = SuccessfulFakeRepository()
    use_case = JokeUseCase(repository)
    joke = use_case.get_random_joke()

    assert joke.joke_id is None
    assert joke.content is not None
    assert joke.type == "joke"


def test_get_joke_by_id_failed():
    repository = NotFoundFakeRepository()
    use_case = JokeUseCase(repository)

    with pytest.raises(RuntimeError):
        joke = use_case.get_joke_by_id(1)


def test_get_joke_by_id_successful():
    repository = SuccessfulFakeRepository()
    use_case = JokeUseCase(repository)
    joke = use_case.get_joke_by_id(5)

    assert joke.joke_id == 5
    assert joke.content is not None
    assert joke.type == "joke"


def test_create_joke():
    repository = SuccessfulFakeRepository()
    use_case = JokeUseCase(repository)
    joke = use_case.create_joke("a basic joke")

    assert joke.joke_id == 1
    assert joke.content == "a basic joke"
    assert joke.type == "joke"


def test_edit_joke_successful():
    repository = SuccessfulFakeRepository()
    use_case = JokeUseCase(repository)
    joke = use_case.edit_joke(1, "a basic joke 2")

    assert joke.joke_id == 1
    assert joke.content == "a basic joke 2"
    assert joke.type == "joke"


def test_edit_joke_failed():
    repository = NotFoundFakeRepository()
    use_case = JokeUseCase(repository)

    with pytest.raises(RuntimeError):
        use_case.edit_joke(1, "a basic joke 2")


def test_delete_joke_successful():
    repository = SuccessfulFakeRepository()
    use_case = JokeUseCase(repository)

    use_case.delete_joke(1)


def test_delete_joke_failed():
    repository = NotFoundFakeRepository()
    use_case = JokeUseCase(repository)

    with pytest.raises(RuntimeError):
        use_case.delete_joke(1)
