import os
import jwt
from fastapi.security import HTTPAuthorizationCredentials


class Token:

    @staticmethod
    def encode(payload: dict):
        return jwt.encode(payload, os.getenv('JWT_SECRET'), algorithm=os.getenv('JWT_ALGORITHM'))

    @staticmethod
    def decode(token: HTTPAuthorizationCredentials):
        return jwt.decode(token.credentials, os.getenv('JWT_SECRET'), algorithms=[os.getenv('JWT_ALGORITHM')])