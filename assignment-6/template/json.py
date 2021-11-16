from flask import Flask,jsonify
import demjson

app=Flask(__name__)

employee_db=[
     {
         "id":1,
         "name":"Arun",
         "salary":1000,
         "email":"arun@gmail.com",
         "course":"Python"
     },
     {
         "id":2,
         "name":"Hari",
         "salary":2000,
         "email":"hari@gmail.com",
         "course":"Java"
     },
     {
         "id":3,
         "name":"Manish",
         "salary":3000,
         "email":"arun@gmail.com",
         "course":"C++"
     },
     {
         "id":4,
         "name":"Varun",
         "salary":4000,
         "email":"arun@gmail.com",
         "course":"Django"
     },
     {
         "id":5,
         "name":"Suman",
         "salary":5000,
         "email":"suman@gmail.com",
         "course":"Csharp"
     }
         ]

#retrieve all the employee details
@app.route("/employee")
def employee_details():
    employee_details=demjson.encode(employee_db)

    return jsonify({'employee':employee_details})

if __name__=='__main__':
    app.run(debug=True)