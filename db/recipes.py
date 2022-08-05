import datetime
import sqlalchemy
from sqlalchemy.orm import relationship
from .base import metadata
from .recipe_tags import recipe_tags

recipes = sqlalchemy.Table(
    "recipes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
    sqlalchemy.Column("likes_count", sqlalchemy.Integer),
    sqlalchemy.Column("dish_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('dishes.id'), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("cooking_steps", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("image", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)
