from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True

class Token(BaseModel):
    """Схема для возврата JWT токена."""
    access_token: str
    token_type: str = "bearer"

