from flask import Flask,request
from flask_restful import Api, Resource
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs

flask_app=Flask(__name__)
app=flask_app
api=Api(app)


class EmployeeRequestSchema(Schema):
    emp_id = fields.Integer(required=True, description="This is employee-id")
    emp_name = fields.String(required=True, description="employee-name")
    emp_salary = fields.Float(required=False, description="employee-salary")
    emp_email = fields.String(required=True, description="employee-email address")
    

class MainClass(MethodResource,Resource):
    def get(self):
        return {"KEY":"GET"}
    @use_kwargs(EmployeeRequestSchema,location=('json'))
    def post(self,*args,**kwrgs):
        print(request.get_json())
        return {"KEY":"POST"}
    
    

api.add_resource(MainClass,"/api")
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Employee-details',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

docs.register(MainClass)
if __name__=="__main__":
    app.run(debug=True)
        
     