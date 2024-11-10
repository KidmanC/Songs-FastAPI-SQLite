from pydantic import BaseModel

class Song(BaseModel):
    #id: int | None = None
    title: str | None = None
    artist: str | None = None
    album: str | None = None
    year: int | None = None
    genre: str | None = None
    duration: str | None = None