import unittest
from unittest.mock import patch
import json
import logging
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs
from flask import Flask,request
from flask_apispec.views import MethodResource
from flask_restful import Api, Resource

import sys
sys.path.append("d:/py-assignments-new/py-assignments/assignment-7/")
from app import app

logging.basicConfig(level=logging.DEBUG)

class EmployeeRequestSchema(Schema):
    emp_id = fields.Integer(required=True, description="This is employee-id")
    emp_name = fields.String(required=True, description="employee-name")
    emp_salary = fields.Float(required=False, description="employee-salary")
    emp_email = fields.String(required=True, description="employee-email address")


class Testemployee(unittest.TestCase):         
    def setUp(self):
        self.app = app.test_client()
        
    def test_get(self):
        payload=json.dumps({"KEY":"GET"})
        
        response = self.app.get('/emp-api', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
        
    def test_stu_get(self):
        payload=json.dumps({"KEY":"GET"})
        
        response = self.app.get('/stu-api', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
        
        
    
    def setUp(self):
        self.app = app.test_client()
        
    @use_kwargs(EmployeeRequestSchema,location=('json'))
    def test_emp_post(self,*args,**kwrgs):
        logging.debug(request.get_json())
        payload = json.dumps({"KEY":"POST"})
        
        response = self.app.post('/emp-api', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
        
if __name__=='__main__':
   unittest.main() 