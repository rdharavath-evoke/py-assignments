from typing import Text
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base


class Movie(Base):
    __tablename__ = "Movie_details"
    id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String)
    location = Column(String)
    theatre = Column(String)
    ticket_cost = Column(String)
        
        