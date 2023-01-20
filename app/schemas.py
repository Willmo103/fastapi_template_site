from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


class UserNew(BaseModel):
    email: EmailStr
    password: str
    username: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(UserNew):
    ...


class TokenData(BaseModel):
    id: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class MemeData(BaseModel):
    url: str


class AdminUser(BaseModel):
    secret: str
