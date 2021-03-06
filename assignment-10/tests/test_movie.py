
from fastapi.testclient import TestClient
import json

 
import sys
sys.path.append("d:/py-assignments-new/py-assignments/assignment-10/")
from main import MovieList, app, delete_movie

    

client = TestClient(app)
    
    
def test_get_movie():
    response = client.get('/movie?page=1&size=10')
    assert response.status_code == 200

def test_create_movie():
    movie_data = {
        "movie_name"  : "RRR",
        "location"    : "Uppal",
        "theatre"     : "Asian",
        "ticket_cost" : "100"}
        
    response=client.post('/movie',data=json.dumps(movie_data))
    assert response.status_code == 200
    
def test_update_movie():
    movie_data = {
        "movie_name"  : "Bahubali",
        "location"    : "Lbnagar",
        "theatre"     : "shiva",
        "ticket_cost" : "100"}
    
        
    response=client.post('/movie',data=json.dumps(movie_data))
    assert response.status_code == 200
    

def test_delete_movie():
    response = client.delete('/movie/1')
    assert response.status_code == 200
        
