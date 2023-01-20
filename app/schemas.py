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
    username: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserSelf(UserOut):
    password: str

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
