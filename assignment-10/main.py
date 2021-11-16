from fastapi import FastAPI,Depends,Request, requests
import models
from database import engine

from scheemas import MovieList,MovieCreate,MovieDelete,MovieUpdate
from typing import List
from database import engine
from models import Movie
import database
from sqlalchemy.orm import Session

from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination import PaginationParams, Page
from fastapi.responses import JSONResponse
import logging
logging.basicConfig(level=logging.DEBUG)


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

models.Base.metadata.create_all(bind=engine)




@app.get("/movie", response_model=Page[MovieList])
def Get_limitation_of_Movie_Details(page:int,size:int,database:Session=Depends(database.get_db)):
    logging.debug("page:",page,"size:",size)
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


@app.delete("/movie/{movieId}")
def delete_movie(movieId, database:Session=Depends(database.get_db)):
    # query = Movie.delete().where(Movie.id==movie.id)
    # database.delete(query)
    # return query
    movie_data = database.query(Movie).filter(Movie.id==movieId)
    if movie_data.first():
        movie_data.delete(synchronize_session=False)
    else:
        return f"Movie with {movieId} is not found"
    database.commit()
    return "Movie Deleted Successfully!"

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=200,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


add_pagination(app)