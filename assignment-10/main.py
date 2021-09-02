from fastapi import FastAPI,Depends
import models
from database import engine

from scheemas import MovieList,MovieCreate,MovieDelete,MovieUpdate
from typing import List
from database import engine
from models import Movie
import database
from sqlalchemy.orm import Session

from fastapi_pagination import Page, add_pagination, paginate


app = FastAPI()

models.Base.metadata.create_all(bind=engine)




@app.get("/movie", response_model=Page[MovieList])
def Get_limitation_of_Movie_Details(database:Session=Depends(database.get_db)):
    return paginate(database.query(Movie).all())
    
@app.post("/movie",response_model=MovieList)
def create_movie(movie: MovieCreate,database:Session=Depends(database.get_db)):
    
        details=Movie(
            movie_name=movie.movie_name,
            location=movie.location,
            theatre=movie.theatre,
            ticket_cost="100"
        )
        database.add(details)
        database.commit()
        database.refresh(details)
        return details


# @app.get("/movie/{movieId}", response_model=MovieList)
# async def find_movie_by_id(movieId:str):
#     query = Movie.select().where(Movie.c.id==movieId)
#     database.fetch_one(query)
#     database.commit()
#     return query


@app.put("/movie",response_model=MovieList)
def update_movie(movie: MovieUpdate,database:Session=Depends(database.get_db)):
    
    query = Movie.update().where(Movie.c.id==movie.id).values(
            movie_name =movie.movie_name,
            location=movie.location,
            theatre=movie.theatre,
            ticket_cost=movie.ticket_cost,
        )
    database.execute(query)
    database.commit()
    database.refresh(query)
    return query


@app.delete("/movie/{movieId}", response_model=MovieList)
def delete_movie(movie: MovieDelete,database:Session=Depends(database.get_db)):
    query = Movie.delete().where(Movie.c.id==movie.id)
    database.commit()
    return query

add_pagination(app)