from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class Movie(BaseModel):
    name:str
    location:str
    theatre:str

@app.get("/")
def index():
    return {"Key": "value"}

@app.get("/movies")
def get_movies():
    return db

@app.get("/movies/{movie_id}")
def get_movies(movie_id : int):
    return db[movie_id-1]

@app.post("/movies")
def create_movie(movie: Movie):
    db.append(movie.dict())
    return db[-1]

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id : int):
    db.pop(movie_id-1)
    return {}
