from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"data":{"name":"raju"}}

@app.get("/about/{id}")
def abc(id:int):
    return {"data":id}

@app.get("/comment/{id}")
def comments(id):
    return {"data":{"1","2"}}

@app.get("/blogs")
def index(limit, published:bool):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    
class Employee(BaseModel):
    id:int
    name:str
    salary:Optional[bool]
    
@app.post("/employee")
def create_employee(request:Employee):
    return {"data":f"employee {request.id} is created"}