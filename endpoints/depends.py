from fastapi import Depends, HTTPException, status
from db.base import database
from models.user import User
from repositories.users import UserRepository
from repositories.admin import AdminRepository
from repositories.recipes import RecipeRepository
from core.security import JWTBearer, decode_access_token


def get_recipe_repository() -> RecipeRepository:
    return RecipeRepository(database)


def get_admin_repository() -> AdminRepository:
    return AdminRepository(database)


def get_user_repository() -> UserRepository:
    return UserRepository(database)


async def get_current_user(
    users: UserRepository = Depends(get_user_repository),
    token: str = Depends(JWTBearer()),
) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    username: str = payload.get("sub")
    if username is None:
        raise cred_exception
    user = await users.get_by_username(username=username)
    if user is None:
        return cred_exception
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is blocked")
    return user
