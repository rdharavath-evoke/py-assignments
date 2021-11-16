from flask import Flask,request
# appFlask = Flask(__name__)

from flask_restful import Api, Resource
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs

app = Flask(__name__)
api=Api(app)

def rates(amount):
        try:
            if amount<=3000000:
                rate=6.5
                return rate
            elif 3000000<amount<=5000000:
                rate=7.5
                return rate
            elif 5000000<amount<=9000000:
                rate=9.0
                return rate
        except Exception: 
            return '''More than 90Laks, there is no loans'''
        



class homeloanrequestscheema(Schema):
    Loanamount = fields.Integer(required=True, description="Home Loan Amount")
    Tenure=fields.Integer(required=True,description="Tenure(no.of Years)")
    rate=rates(Loanamount)


def total_interest(Loanamount,Tenure,rate):
    si = (Loanamount * Tenure * rate)/100
    return si



@use_kwargs(homeloanrequestscheema,location=('json'))
class MainClass(MethodResource,Resource):    
    def post(self,*args,**kwrgs):
        request_data = request.get_json()
        Loanamount = request_data['Loanamount']
        time=request_data['Tenure']
        rate=rates(Loanamount)
        if 9000000>Loanamount:
            Total_interest=total_interest(Loanamount,time,rate)
            Total_amount=Total_interest+Loanamount
        
            return {"total_interest":Total_interest,"total_amount":Total_amount}
        else:
            return {"more than 90Laks there is no homeloans ":
                "please select the amount less than 90Lakhs"}
        


api.add_resource(MainClass,"/api")
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='GetLoanDetails',
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