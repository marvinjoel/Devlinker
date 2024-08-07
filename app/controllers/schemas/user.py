from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    email: str
    hashed_password: str
    is_recruiter: bool