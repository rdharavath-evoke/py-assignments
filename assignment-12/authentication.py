import os
from flask import Flask,request,jsonify, make_response
from flask_restful import Api, Resource
from flask_apispec import marshal_with, doc, use_kwargs

from geopy.geocoders import Nominatim
import json
from flask_sqlalchemy import SQLAlchemy
import uuid # for public id
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask_migrate import Migrate


flask_app=Flask(__name__)
app=flask_app
api=Api(app)

app.config['SECRET_KEY'] = 'your secret key'
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Rdr563455@localhost:1056/employee'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# creates SQLALCHEMY object
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# manager.add_command('db', MigrateCommand)

# Database ORMs
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(255))


# Decarator for verifying   
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user = User.query\
                .filter_by(id = data['public_id'])\
                .first()
        except Exception as exc:
            print(exc)
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated
  

# User Database Route
# this route sends back list of users users
@app.route('/user', methods =['GET'])
@token_required
def get_all_users(current_user):
    # querying the database
    # for all the entries in it
    users = User.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json
        # to the response list
        output.append({
            'public_id': user.id,
            'email' : user.email
        })
  
    return jsonify({'users': output})


@app.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    
    auth = json.loads(request.data)
  
    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = User.query\
        .filter_by(email = auth.get('email'))\
        .first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'public_id': user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'],algorithm="HS256")
        return make_response(jsonify({'token' : token}), 201)
    # returns 403 if password is wrong
    return {"Status":
        403,
        'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}


# signup route
@app.route('/signup', methods =['POST'])
def signup():
    # creates a dictionary of the form data
    data = json.loads(request.data)

    # gets name, email and password
    email = data.get('email')
    password = data.get('password')
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        # database ORM object
        user = User(
            id = 1,
            email = email,
            password = generate_password_hash(password)
        )
        # insert user
        db.session.add(user)
        db.session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)



@app.route("/api/rating",methods=['POST'])
@token_required
def Getrating(user):
        try:
            request_data = json.loads(request.data)
            total_years = request_data['total_years']
            compony_count=request_data['company_count']
            value=total_years/compony_count
            if value>2:
                rating=5
                return jsonify({"rating":rating})
            elif 1.5<value<=2:
                rating=4
                return jsonify({"rating":rating})
            elif 1<value<=1.5:
                rating=3
                return jsonify({"rating":rating})
            elif 0.5<value<=1:
                rating=2
                return jsonify({"rating":rating})
            elif 0<value<=0.5:
                rating=1
                return jsonify({"rating":rating})
            elif value<0:
                rating=0
                return jsonify({"rating":rating})
            else:
                return jsonify({"rating":0})

        except Exception as exc:
            return jsonify({"Status":500,"Exception":str(exc)})




@app.route("/api/location",methods=["POST"])
@token_required
def getLocation(user):
    try:
        request_data = json.loads(request.data)
        address = request_data['address']
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(address)
        if location:
            return {"location":location.address,
                "latitude":location.latitude,
                "longitude":location.longitude}
        return {}
    except Exception as exc:
        return jsonify({"Status":500,"Exception":str(exc)})


# api.add_resource(MainClass,"/api/rating")
# api.add_resource(MainClass2,"/api/location")

if __name__=="__main__":
    app.run(debug=True)