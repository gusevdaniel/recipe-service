import datetime
from .base import BaseRepository
from db.users import users
from db.recipes import recipes
from models.user import User
from models.admin import Admin
from models.recipe import Recipe


class AdminRepository(BaseRepository):

    async def update_user(self, id: int, a: Admin) -> User:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query)
        user = User.parse_obj(user)
        user.is_active = a.is_active
        user.updated_at = datetime.datetime.utcnow()
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)
        return user

    async def update_recipe(self, id: int, a: Admin) -> Recipe:
        query = recipes.select().where(recipes.c.id == id)
        recipe = await self.database.fetch_one(query)
        recipe = Recipe.parse_obj(recipe)
        recipe.is_active = a.is_active
        recipe.updated_at = datetime.datetime.utcnow()
        values = {**recipe.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = recipes.update().where(recipes.c.id == id).values(**values)
        await self.database.execute(query)
        return recipe
