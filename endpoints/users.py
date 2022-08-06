from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from repositories.users import UserRepository
from models.user import User, UserIn, UserProfile
from .depends import get_user_repository, get_current_user

router = APIRouter()


@router.post("/create", response_model=User)
async def create_user(
    user: UserIn,
    users: UserRepository = Depends(get_user_repository)
):
    check_user = await users.get_by_username(username=user.username)
    if check_user is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="This username already exists")
    return await users.create(u=user)


@router.put("/{id}/update", response_model=User)
async def update_user(
    id: int,
    user: UserIn,
    users: UserRepository = Depends(get_user_repository),
    current_user: User = Depends(get_current_user)
):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.username != current_user.username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)


@router.get("/{id}", response_model=UserProfile)
async def read_user(
    id: int,
    users: UserRepository = Depends(get_user_repository),
):
    user = await users.get_by_id(id=id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    user_profile = await users.get_profile(user)
    return user_profile


@router.get("/", response_model=List[UserProfile])
async def read_users(
    users: UserRepository = Depends(get_user_repository),
    limit: int = 10
):
    active_users_objects = await users.get_active(limit=limit)
    active_users = []
    for obj in active_users_objects:
        user_profile = await users.get_profile(obj)
        user_profile = {**user_profile.dict()}
        active_users.append(user_profile)
    active_users = sorted(active_users, key=lambda x: x['recipes_count'], reverse=True)
    return active_users
