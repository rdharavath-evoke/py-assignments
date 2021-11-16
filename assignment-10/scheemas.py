
from database import Base
from pydantic import BaseModel, Field
from typing import Optional


class MovieList(BaseModel):
    id          : int
    movie_name  : str
    location    : str
    theatre     : str
    ticket_cost : str
    
    class Config:
        orm_mode = True

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
    id          : int 
    