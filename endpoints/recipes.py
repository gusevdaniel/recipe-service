from typing import List
from models.recipe import Recipe, RecipeIn
from models.user import User
from repositories.recipes import RecipeRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_recipe_repository, get_current_user

router = APIRouter()


@router.post("/", response_model=Recipe)
async def create_recipe(
    r: RecipeIn,
    recipes: RecipeRepository = Depends(get_recipe_repository),
    current_user: User = Depends(get_current_user)
):
    return await recipes.create(user_id=current_user.id, r=r)


@router.get("/", response_model=List[Recipe])
async def read_recipes(
    limit: int = 100,
    skip: int = 0,
    recipes: RecipeRepository = Depends(get_recipe_repository)):
    return await recipes.get_all(limit=limit, skip=skip)


@router.put("/", response_model=Recipe)
async def update_recipe(
    id: int,
    r: RecipeIn,
    recipes: RecipeRepository = Depends(get_recipe_repository),
    current_user: User = Depends(get_current_user)
):
    recipe = await recipes.get_by_id(id=id)
    if recipe is None or recipe.user_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return await recipes.update(id=id, user_id=current_user.id, r=r)


@router.delete("/")
async def delete_recipe(
    id: int,
    recipes: RecipeRepository = Depends(get_recipe_repository),
    current_user: User = Depends(get_current_user)
):
    recipe = await recipes.get_by_id(id=id)
    if recipe is None or recipe.user_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    result = await recipes.delete(id=id)
    return {"status": True}
