from sqlalchemy import String, Integer, Column
from .database import Base

class Movie(Base):
    __tablename__="movie"
    
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    title=Column(String)
    
class User(Base):
    __tablename__="user"
    
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    
