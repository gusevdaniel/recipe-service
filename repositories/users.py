import datetime
from typing import List, Optional
from .base import BaseRepository
from db.users import users
from models.user import User, UserIn
from core.security import hash_password


class UserRepository(BaseRepository):

    async def create(self, u: UserIn) -> User:
        user = User(
            username=u.username,
            hashed_password=hash_password(u.password),
            is_active=True,
            favorites_count=0,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            username=u.username,
            hashed_password=hash_password(u.password),
            is_active=True,
            favorites_count=0,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)
        return user

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_username(self, username: str) -> Optional[User]:
        query = users.select().where(users.c.username == username)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
