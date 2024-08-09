import os
import jwt


class Token:

    @staticmethod
    def encode(payload: dict):
        return jwt.encode(payload, os.getenv('JWT_SECRET'), algorithm=os.getenv('JWT_ALGORITHM'))

    @staticmethod
    def decode(token: str):
        return jwt.decode(token, os.getenv('JWT_SECRET'), algorithm=os.getenv('JWT_ALGORITHM'))