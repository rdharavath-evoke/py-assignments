import databases, sqlalchemy, uuid
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from sqlalchemy import engine

## Postgres Database

DATABASE_URL="postgresql://postgres:Rdr563455@127.0.0.1:1056"
database=databases.Database(DATABASE_URL)
metadata=sqlalchemy.MetaData()

users=sqlalchemy.Table(
                         "movie_details",
                         metadata,
                         sqlalchemy.Column("id",sqlalchemy.String, primary_key=True),
                         sqlalchemy.Column("movie_name",sqlalchemy.String),
                         sqlalchemy.Column("location",sqlalchemy.String),
                         sqlalchemy.Column("theatre",sqlalchemy.String),
                         sqlalchemy.Column("ticket_cost",sqlalchemy.String),
                      )

engine=sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


##Models
class MovieList(BaseModel):
    id          : str
    movie_name  : str
    location    : str
    theatre     : str
    ticket_cost : str

class MovieCreate(BaseModel):
    movie_name  : str = Field(..., example="Avengers")
    location    : str = Field(..., example="Uppal")
    theatre     : str = Field(..., example="Asians")
    ticket_cost : str = Field(..., example="100")
    
class MovieUpdate(BaseModel):
    id          : str = Field(..., example="enter id")
    movie_name  : str = Field(..., example="Avengers")
    location    : str = Field(..., example="Uppal")
    theatre     : str = Field(..., example="Asians")
    ticket_cost : str = Field(..., example="100")
    
class MovieDelete(BaseModel):
    id          : str = Field(...,example="Enter id")
    
    
app=FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/movie",response_model=List[MovieList])
async def Get_All_Movie_Details():
    query=users.select()
    return await database.fetch_all(query)


@app.post("/movie",response_model=MovieList)
async def create_movie(movie: MovieCreate):
    gID = str(uuid.uuid1())
    query = users.insert().values(
        id=gID,
        movie_name=movie.movie_name,
        location=movie.location,
        theatre=movie.theatre,
        ticket_cost="100"
    )
    await database.execute(query)
    return {
        "id" : gID,
        **movie.dict(),
        "ticket_cost":"100"
    }


@app.get("/movie/{movieId}", response_model=MovieList)
async def find_movie_by_id(movieId:str):
    query = users.select().where(users.c.id==movieId)
    return await database.fetch_one(query)


@app.put("/movie",response_model=MovieList)
async def update_movie(movie: MovieUpdate):
    query = users.update().\
        where(users.c.id==movie.id).\
        values(
            movie_name =movie.movie_name,
            location=movie.location,
            theatre=movie.theatre,
            ticket_cost=movie.ticket_cost,
        )
    await database.execute(query)
    return await find_movie_by_id(movie.id)


@app.delete("/movie/{movieId}")
async def delete_movie(movie: MovieDelete):
    query = users.delete().where(users.c.id==movie.id)
    await database.execute(query)
    return {
        "status" : "True",
        "msg" : "This movie has been deleted successfully."
    }