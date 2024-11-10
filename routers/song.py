from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from schemas.song import Song
from config.dbase import session
from services.song import SongService

song_router = APIRouter()

@song_router.get('/songs', tags=["Songs"])
def get_songs():
    db = session()
    query = SongService(db).get_songs()
    return JSONResponse(content=jsonable_encoder(query), status_code=200)

@song_router.get('/songs/{song_id}', tags=["Songs"])
def get_song(song_id: int):
    db = session()
    song = SongService(db).get_song(song_id)
    if not song:
        return JSONResponse(content={'error': 'Song not found'}, status_code=404)
    return JSONResponse(content=jsonable_encoder(song), status_code=200)
    

@song_router.get('/songs/', tags=["Songs"])
def get_songs_by_genre(genre: str):
    db = session()
    query = SongService(db).get_songs_by_genre(genre)
    if not query:
        return JSONResponse(content={'error': 'Genre not found'}, status_code=404)
    return JSONResponse(content= jsonable_encoder(query), status_code=200)

@song_router.post('/songs', tags=["Songs"])
def add_song(song: Song):
    db = session()
    query = SongService(db).add_song(song)
    return JSONResponse(content = {'message': 'Song added successfully'}, status_code=201)

@song_router.put('/songs/{song_id}', tags=["Songs"])

def update_song(song_id: int, song: Song):
    db = session()
    query = SongService(db).update_song(song_id, song)
    if not query:
        return JSONResponse(content={'error': 'Song not found'}, status_code=404)
    return JSONResponse(content = {'message': 'Song updated successfully'}, status_code=200)

@song_router.delete('/songs/{song_id}', tags=["Songs"], dependencies = [Depends(JWTBearer())])

def delete_song(song_id: int):
    db = session()
    song = SongService(db).delete_song(song_id)
    if not song:
        return JSONResponse(content={'error': 'Song not found'}, status_code=404)
    return JSONResponse(content = {'message': 'Song deleted successfully'}, status_code=200)