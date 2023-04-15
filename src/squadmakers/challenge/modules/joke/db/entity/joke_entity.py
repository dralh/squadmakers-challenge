from sqlalchemy import BigInteger, Column, String, Table

from squadmakers.challenge.database.sqlalchemy import metadata

__all__ = ["joke_table"]


joke_table = Table(
    "joke",
    metadata,
    Column(
        "joke_id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    ),
    Column(
        "content",
        String,
        nullable=False,
    ),
    schema="challenge",
)
