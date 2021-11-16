import unittest
from unittest.mock import patch
import json
import logging

import sys
sys.path.append("d:/py-assignments-new/py-assignments/assignment-5/")
from swagger_app import app

logging.basicConfig(level=logging.DEBUG)

class TestHomeloan(unittest.TestCase):         
    def setUp(self):
        self.app = app.test_client()
        
    def test_homeloan(self):
        payload = json.dumps({
            "Loanamount": 10000,
            "Tenure": 3
        })
        response = self.app.post('/api', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
        
if __name__=='__main__':
   unittest.main() 