from pydantic import BaseModel


class Admin(BaseModel):
    token: str
    is_active: bool
