from sqlalchemy.orm import registry

__all__ = ["mapper_registry"]

mapper_registry = registry()
