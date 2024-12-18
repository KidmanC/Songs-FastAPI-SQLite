from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from utils.jwt_handler import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['username'] != 'user123':
            raise HTTPException(status_code=403, detail="Invalid user")