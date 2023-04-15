from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from squadmakers.challenge.config import config

__all__ = ["Session"]


sqlalchemy_config = config.get("Sqlalchemy")
engine = create_engine(sqlalchemy_config.get("DATABASE_URI"))
Session = scoped_session(sessionmaker(bind=engine))
