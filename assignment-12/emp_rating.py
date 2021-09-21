from flask import Flask,request
from flask_restful import Api, Resource
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from geopy import location
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs

from geopy.geocoders import Nominatim

flask_app=Flask(__name__)
app=flask_app
api=Api(app)

def rating(value):
        try:
            if value>2:
                rating=5
                return rating
            elif 1.5<value<=2:
                rating=4
                return rating
            elif 1<value<=1.5:
                rating=3
                return rating
            elif 0.5<value<=1:
                rating=2
                return rating
            elif 0<value<=0.5:
                rating=1
                return rating
            elif value<0:
                rating=0
                return rating
                
        except Exception: 
            return '''No ratings'''




class EmployeeRequestSchema(Schema):
    total_years = fields.Integer(required=True, description="total no of years")
    compony_count=fields.Integer(required=True,description="total no of componies")


class MainClass(MethodResource,Resource):
    @use_kwargs(EmployeeRequestSchema,location=('json'))
    def post(self,*args,**kwrgs):
        request_data = request.get_json()
        total_years = request_data['total_years']
        compony_count=request_data['compony_count']
        value=total_years/compony_count
        ratings=rating(value)
        return {"rating":ratings}


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