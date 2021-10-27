from fastapi import FastAPI,status, Response, Form
from fastapi.params import Depends
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from passlib.utils.decor import deprecated_method
from . import models, schemas
from . database import SessionLocal, engine
from sqlalchemy.orm import Session, query
from typing import List
from . hashing import Hash



app=FastAPI()


models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

        




@app.get("/Movie/{id}", response_model=schemas.showMovie, tags=['Movies'])
def show(id, response:Response, db: Session = Depends(get_db)):
    movie=db.query(models.Movie).filter(models.Movie.id==id).first()
    if not movie:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {f"Movie with id {id} is not available"}
    return movie

@app.delete("/Movie/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Movies'])
def destroy(id, db : Session=Depends(get_db)):
    db.query(models.Movie).filter(models.Movie.id==id).delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

@app.put("/Movie/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['Movies'])
def update(id, response:Response,request: schemas.Movie, db:Session=Depends(get_db)):
    movie=db.query(models.Movie).filter(models.Movie.id==id)
    if not movie.first():
        response.status_code=status.HTTP_404_NOT_FOUND,
        return f"Movie with id {id} not found"
    movie.update(request)     
    db.commit()
    return "updated"
    




@app.post("/user", tags=['users'])
def user(request:schemas.User, db:Session=Depends(get_db)):
    
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/{id}", response_model=schemas.showUser, tags=['users'])
def get_user(id:int, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id {id} is not available")
    return user
