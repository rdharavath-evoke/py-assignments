from typing import List
from fastapi import APIRouter, Depends,status,Response
from fastapi.exceptions import HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import movie

import blog

router=APIRouter(
    tags=["movies"]
    
)

get_db=database.get_db

@router.get("/Movie")
def getall(db: Session = Depends(get_db)):
    return movie.get_all(db)


@router.post('/Movie',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Movie, db: Session = Depends(get_db)):
    return movie.create(request, db)
    


@router.get("/Movie/{id}", response_model=schemas.showMovie)
def show(id:int, response:Response, db: Session = Depends(get_db)):
    return movie.show(id,db,response)

@router.delete("/Movie/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session=Depends(get_db)):
    return movie.destroy(id,db)

@router.put("/Movie/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id:int, response:Response,request: schemas.Movie, db:Session=Depends(get_db)):
    return movie.update(id,db,request,response)