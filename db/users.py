import datetime
import sqlalchemy
from .base import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("username", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean),
    sqlalchemy.Column("favorites_count", sqlalchemy.Integer),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
)
