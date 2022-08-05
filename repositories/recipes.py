import datetime
from typing import List, Optional
from sqlalchemy import or_
from models.recipe import Recipe, RecipeIn
from db.recipes import recipes
from .base import BaseRepository


class RecipeRepository(BaseRepository):

    async def create(self, user_id: int, r: RecipeIn) -> Recipe:
        recipe = Recipe(
            user_id=user_id,
            is_active=True,
            likes_count=0,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            name=r.name,
            dish_id=r.dish_id,
            description=r.description,
            cooking_steps=r.cooking_steps,
            image=r.image
        )
        values = {**recipe.dict()}
        values.pop("id", None)
        query = recipes.insert().values(**values)
        recipe.id = await self.database.execute(query=query)
        return recipe

    async def update(self, id: int, user_id: int, r: RecipeIn) -> Recipe:
        recipe = Recipe(
            id=id,
            user_id=user_id,
            is_active=True,
            likes_count=0,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            name=r.name,
            dish_id=r.dish_id,
            description=r.description,
            cooking_steps=r.cooking_steps,
            image=r.image
        )
        values = {**recipe.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        query = recipes.update().where(recipes.c.id == id).values(**values)
        await self.database.execute(query=query)
        query = recipes.select().where(recipes.c.id == id)
        old_recipe = await self.database.fetch_one(query)
        recipe.created_at = old_recipe.created_at
        return recipe

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Recipe]:
        query = recipes.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_active(self, filter: Optional[str] = None, limit: int = 100, skip: int = 0) -> List[Recipe]:
        if filter is None:
            query = recipes.select().where(recipes.c.is_active == True).limit(limit).offset(skip)
        else:
            query = recipes.select().where(
                recipes.c.is_active == True
            ).filter(
                or_(recipes.c.name.contains(filter),
                    recipes.c.name.contains(filter.lower()),
                    recipes.c.name.contains(filter.capitalize())
                    )
            ).limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = recipes.delete().where(recipes.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Recipe]:
        query = recipes.select().where(recipes.c.id == id)
        recipe = await self.database.fetch_one(query)
        if recipe is None:
            return None
        return Recipe.parse_obj(recipe)
