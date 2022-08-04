import datetime
from typing import Optional
from pydantic import BaseModel, validator, constr


class User(BaseModel):
    id: Optional[str] = None
    username: str
    is_active: Optional[bool] = None
    favorites_count: Optional[int] = None
    hashed_password: str
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None


class UserIn(BaseModel):
    username: str
    password: constr(min_length=8)
    password2: str

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v
