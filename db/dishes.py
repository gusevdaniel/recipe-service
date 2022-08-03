import sqlalchemy
from .base import metadata

dishes = sqlalchemy.Table(
    "dishes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False, unique=True),
)
