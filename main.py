from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from config.dbase import base, engine
from middlewares.error_handler import errorHandler
from routers.song import song_router
from routers.user import user_router

app = FastAPI()
app.title = "My First FastAPI App"
app.description = "This is my first FastAPI app. I hope you enjoy it!"
app.version = "0.0.1"

app.add_middleware(errorHandler)
app.include_router(song_router)
app.include_router(user_router)

#db
base.metadata.create_all(bind=engine)



@app.get('/', tags=["Home"])
def read_root():
    return HTMLResponse(content="<h1>Welcome to my first FastAPI app!</h1>", 
                        status_code=200)


