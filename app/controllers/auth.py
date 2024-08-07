import os
import bcrypt

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.exceptions import BadRequestException
from controllers.schemas.user import UserInput
from models.db.db_setup import db_session
from models.user import User

authRouter = APIRouter(
    prefix=os.getenv('API_PREFIX'),
    tags=['auth']
)


@authRouter.post("/auth/users")
async def create_user(request: UserInput, db: Session = Depends(db_session)) -> UserInput:
    exist = db.query(User).filter(User.email == request.email).first()
    if exist:
        raise BadRequestException("Email ya existe")

    password = bytes(request.hashed_password, 'utf-8')
    request.hashed_password = str(bcrypt.hashpw(password, bcrypt.gensalt(rounds=10)), 'utf-8')
    item = User(**request.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item