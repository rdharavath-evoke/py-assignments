from flask import Flask,request
from flask_restful import Api, Resource
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs
    
from starlette.responses import StreamingResponse,Response
from flask.views import MethodView, View
from flask import send_file


from fpdf import FPDF


appFlask = Flask(__name__)
app=appFlask
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

def total_interest(Loanamount,Tenure,rate):
    si = (Loanamount * Tenure * rate)/100
    return si

class homeloanrequestscheema(Schema):
    Loanamount = fields.Integer(required=True, description="Home Loan Amount")
    Tenure=fields.Integer(required=True,description="Tenure(no.of Years)")
    rate=rates(Loanamount)

@use_kwargs(homeloanrequestscheema,location=('json'))
class MainClass(MethodView): 
    
    def post(self,*args,**kwrgs):
        request_data = request.get_json()
        Loanamount = request_data['loan amount']
        time=request_data['Tenure(no.of Years)']
        rate=rates(Loanamount)
        Total_interest=total_interest(Loanamount,time,rate)
        Total_amount=Total_interest+Loanamount
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        f = open("getloandetails.txt", "r")
        
  
        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 8, txt = x, ln = 1, align = 'L')
        pdf.output("getloandetails.pdf") 
       
        return send_file(f.name.replace(".txt",".pdf"),mimetype="application/octet_stream",as_attachment=True,attachment_filename=f.name.replace(".txt",".pdf"))
        


# app.add_resource(MainClass,"/api")
app.add_url_rule('/api/', view_func=MainClass.as_view('show_users'))
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
if __name__=="__main__":
    app.run(debug=True)
    
    

  