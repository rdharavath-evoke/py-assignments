
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


class LocationRequestSchema(Schema):
    address = fields.String(required=True, description="location for given city")


class MainClass(MethodResource,Resource):
    @use_kwargs(LocationRequestSchema,location=('json'))
    def post(self,*args,**kwrgs):
        request_data = request.get_json()
        address = request_data['address']
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(address)
        print(request.get_json())
        return [{"location":location.address},
                {"latitude":location.latitude},
                {"longitude":location.longitude}]



api.add_resource(MainClass,"/api")
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Location-details',
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