from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from .. import models

def get_all(db:Session):
    movies=db.query(models.Movie).all()
    return movies


def create(request,db:Session):
    new_movie = models.Movie(name=request.name, title=request.title)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


def destroy(id:int ,db:Session):
    movie=db.query(models.Movie).filter(models.Movie.id==id)
    if not movie.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Movie with id {id} is not found")
    movie.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"


def update(id:int,db:Session,request,response):
    movie=db.query(models.Movie).filter(models.Movie.id==id)
    if not movie.first():
        response.status_code=status.HTTP_404_NOT_FOUND,
        return f"Movie with id {id} not found"
    movie.update(request)     
    db.commit()
    return "updated"


def show(id:int,db:Session,response):
    movie=db.query(models.Movie).filter(models.Movie.id==id).first()
    if not movie:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {f"Movie with id {id} is not available"}
    return movie