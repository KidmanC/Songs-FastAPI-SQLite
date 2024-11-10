from config.dbase import base
from sqlalchemy import Column, Integer, String, ForeignKey


class Song(base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    album = Column(String)
    year = Column(Integer)
    genre = Column(String)
    duration = Column(String)
    #user_id = Column(Integer, ForeignKey('users.id'))