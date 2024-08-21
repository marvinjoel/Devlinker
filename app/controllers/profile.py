import os

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.exceptions import BadRequestException
from models.db.db_setup import db_session
from models.profile import Profile
from services.auth import get_current_user

profile = APIRouter(
    prefix=os.getenv('API_PREFIX'),
    tags=['user']
)


@profile.get("/profile")
async def get_profile(db: Session = Depends(db_session), request: dict = Depends(get_current_user)):

    user_id = request.get("user_id")
    profile = Profile.get_profile(db, user_id)

    if profile is None:
        raise BadRequestException()
    return profile

