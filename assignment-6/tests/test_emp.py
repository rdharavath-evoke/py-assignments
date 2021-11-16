import unittest
from unittest.mock import patch


import sys
sys.path.append("d:/py-assignments-new/py-assignments/assignment-6/")
from app_lx import app

class Testemployee(unittest.TestCase):         
    def setUp(self):
        self.app = app.test_client()
        
        
    def test_employee(self):
        response = self.app.get('/employee')
        self.assertEqual(200, response.status_code)
        
    def test_enternew(self):
        
        response = self.app.post('/enternew')
        self.assertEqual(200, response.status_code)
        
    def test_update(self):
        response = self.app.post('/employeeupdate')
        self.assertEqual(200, response.status_code)
        
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)
    def test_deletemployee(self):
        response = self.app.get('/deleteemployee')
        self.assertEqual(200, response.status_code)
        
    def test_updates(self):
        response = self.app.post('/updates')
        self.assertEqual(200, response.status_code)
    
    
if __name__=='__main__':
   unittest.main() 