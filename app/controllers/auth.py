import os
import traceback

import bcrypt

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from controllers.exceptions import BadRequestException, UnAuthorizedException
from controllers.schemas.user import UserInput, LoginInput
from models.db.db_setup import db_session
from models.token import Token
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


@authRouter.post("/auth/login")
async def login(user_input: LoginInput):
    try:
        with db_session() as db:
            user_name = user_input.user
            user_pwd = user_input.pwd.encode('utf-8')

            user: User = db.query(User).filter(User.username == user_name).first()

            if bcrypt.checkpw(user_pwd, user.hashed_password.encode('utf-8')):
                payload = {
                    'user_id': user.id,
                    'username': user.username,
                    'is_recruiter': user.is_recruiter,
                }
                token = Token.encode(payload=payload)
                return {
                    'user': user_name,
                    'token': f'{token}',
                    'type': 'Bearer'
                }
            else:
                raise UnAuthorizedException()
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        raise UnAuthorizedException()