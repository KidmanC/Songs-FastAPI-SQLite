# This file contains the user router which is responsible for handling the user login request.
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.user import User
from utils.jwt_handler import create_token


user_router = APIRouter()

@user_router.post('/login', tags=["Login"])
def login(user: User):
    if user.username == 'user123' and user.password == 'password123':
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)
    return user