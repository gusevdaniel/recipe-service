import datetime
from typing import Optional
from pydantic import BaseModel


class BaseRecipe(BaseModel):
    name: str
    dish_id: int
    description: str
    cooking_steps: str
    image: str


class Recipe(BaseRecipe):
    id: Optional[str] = None
    user_id: int
    is_active: Optional[bool] = None
    likes_count: Optional[int] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None


class RecipeIn(BaseRecipe):
    pass
