# from sqlalchemy.orm import Session
# from fastapi import HTTPException,status
# from blog import schemas
# from .. hashing import Hash
# from .. import models

# def get(db:Session,id:int):
#     user=db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"User with id {id} is not available")
#     return user