from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional


class UserInput(BaseModel):
    username: str
    email: str
    hashed_password: str
    is_recruiter: bool


class LoginInput(BaseModel):
    user: str
    pwd: str


class UserOutput(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_recruiter: bool
    photo_url: Optional[HttpUrl]
    full_name: Optional[str]
    bio: Optional[str]
    skills: Optional[str]
    experience: Optional[str]

    class Config:
        orm_mode = True