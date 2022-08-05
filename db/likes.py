import sqlalchemy
from .base import metadata

likes = sqlalchemy.Table(
    "likes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column("recipe_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('recipes.id'), nullable=False),
)
