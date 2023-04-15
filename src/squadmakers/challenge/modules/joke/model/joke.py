from dataclasses import dataclass, field

__all__ = ["Joke"]


@dataclass()
class Joke:
    joke_id: int = field(init=False)
    content: int = field(init=False)
    type: str = "joke"
