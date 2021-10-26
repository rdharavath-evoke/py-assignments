from pydantic import BaseModel
from sqlalchemy import orm


class Movie(BaseModel):
    name:str
    title:str

class showMovie(BaseModel):
    name:str
    title:str
    
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str
    
class showUser(BaseModel):
    name:str
    email:str
    
    class Config():
        orm_mode=True


class Login(BaseModel):
    username:str
    password:str
    
    