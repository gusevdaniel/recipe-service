import sqlalchemy
from .base import metadata

recipe_tags = sqlalchemy.Table(
    "recipe_tags",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("recipe_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('recipes.id'), nullable=False),
    sqlalchemy.Column("tag_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('tags.id'), nullable=False),
)
