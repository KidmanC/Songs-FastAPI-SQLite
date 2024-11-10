from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(..., example="user123")
    password: str = Field(..., example="password123")