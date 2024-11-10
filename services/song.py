from models.song import Song as SongModel
from schemas.song import Song

class SongService:
    def __init__(self, db):
        self.db = db

    def get_song(self, song_id):
        return self.db.query(SongModel).filter(SongModel.id == song_id).first()

    def get_songs(self):
        return self.db.query(SongModel).all()

    def get_songs_by_genre(self, genre):
        return self.db.query(SongModel).filter(SongModel.genre == genre).all()
    
    def add_song(self, song: Song):
        new_song = SongModel(**song.dict())
        self.db.add(new_song)
        self.db.commit()
        return new_song

    def update_song(self, song_id, song: Song):
        query = self.db.query(SongModel).filter(SongModel.id == song_id).first()
        if not query:
            return None
        query.title = song.title
        query.artist = song.artist
        query.album = song.album
        query.year = song.year
        query.genre = song.genre
        query.duration = song.duration
        self.db.commit()
        return query

    def delete_song(self, song_id):
        song = self.db.query(SongModel).filter(SongModel.id == song_id).first()
        if not song:
            return None
        self.db.delete(song)
        self.db.commit()
        return song