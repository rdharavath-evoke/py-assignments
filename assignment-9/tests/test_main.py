import unittest
from unittest import mock
from unittest.mock import Mock, patch
import json

import sys
sys.path.append("d:/py-assignments-new/py-assignments/assignment-9/")
from main import app

class TestMoviedetails(unittest.TestCase):         
    def setUp(self):
        self.app = app
        
        
    def test_index(self):
        response = self.app.get('/')
    
    def test_movies(self):
        response = self.app.get('/movies')
        
    def test_moviesdetails(self):
        response = self.app.get('/movies/{movie_id}')

        
    def test_movie(self):
        response = self.app.post('/movies')
        
    def test_deletemovie(self):
        self.app.get('/movies/{movie_id}')
        self.assertEqual(id,id)
            
    
if __name__=='__main__':
   unittest.main() 