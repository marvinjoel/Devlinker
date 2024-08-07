from fastapi import HTTPException
from starlette import status


class UnAuthorizedException(HTTPException):

    def __init__(self, message=None):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Unauthorized access' if message is None else message
        )


class BadRequestException(HTTPException):

    def __init__(self, message=None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Bad Request' if message is None else message
        )