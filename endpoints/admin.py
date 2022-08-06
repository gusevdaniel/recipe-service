from fastapi import APIRouter, Depends, HTTPException, status
from repositories.admin import AdminRepository
from repositories.users import UserRepository
from repositories.recipes import RecipeRepository
from .depends import get_user_repository, get_admin_repository, get_recipe_repository
from models.admin import Admin
from models.user import User
from models.recipe import Recipe
from core.config import ADMIN_KEY

router = APIRouter()


@router.put("/users/{id}/update", response_model=User)
async def update_user(
    id: int,
    admin: Admin,
    admins: AdminRepository = Depends(get_admin_repository),
    users: UserRepository = Depends(get_user_repository)
):
    if admin.token != ADMIN_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    user = await users.get_by_id(id=id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await admins.update_user(id=id, a=admin)


@router.put("/recipes/{id}/update", response_model=Recipe)
async def update_recipe(
    id: int,
    admin: Admin,
    admins: AdminRepository = Depends(get_admin_repository),
    recipes: RecipeRepository = Depends(get_recipe_repository)
):
    if admin.token != ADMIN_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    recipe = await recipes.get_by_id(id=id)
    if recipe is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found recipe")
    return await admins.update_recipe(id=id, a=admin)
