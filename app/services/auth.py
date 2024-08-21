from fastapi import Depends
from fastapi.security import HTTPBearer
from controllers.exceptions import UnAuthorizedException
from models.token import Token
from jwt import InvalidTokenError, ExpiredSignatureError


def get_current_user(token: str = Depends(HTTPBearer())) -> dict:
    try:
        payload = Token.decode(token=token)
        user_id = payload.get("user_id")
        if user_id is None:
            raise UnAuthorizedException()

        return payload

    except InvalidTokenError:
        raise UnAuthorizedException("Invalid token ----")
    except ExpiredSignatureError:
        raise UnAuthorizedException("Token has expired")
