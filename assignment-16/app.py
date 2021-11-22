from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS, cross_origin


app=Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def db_connection():
    conn=None
    try:
        conn=sqlite3.connect('employee.db')
    except sqlite3.error as e:
        print(e)
    return conn

print("connection success")
        
@app.route("/employee", methods=["GET","POST"])
@cross_origin()
def employee():
    conn=db_connection()
    cursor=conn.cursor()
    
    if request.method=="GET":
        cursor=conn.execute("select * from employee")
        employee=[
            dict(id=row[0], fname=row[1], lname=row[2], salary=row[3])
            for row in cursor.fetchall()
        ]  
        if employee is not None:
            return jsonify(employee)   
    
    if request.method=="POST":
        try:
             new_id=request.form["id"]
             new_fname=request.form["fname"]
             new_lname=request.form["lname"]
             new_salary=request.form["salary"]
             
             sql=""" insert into employee (fname, lname, salary, id) values(?,?,?,?)"""
             cursor=cursor.execute(sql,(new_fname, new_lname, new_salary, new_id))
             conn.commit()
             return f"Employee with the id : {cursor.lastrowid} created successfully",201 
        except Exception as e:
            return str(e)
        


@app.route("/employee/<int:id>", methods=["GET","PUT","DELETE"])
@cross_origin()
def single_employee(id):
    conn=db_connection()
    cursor=conn.cursor()
    employee=None
    if request.method=="GET":
        cursor.execute("select * from employee where id=?", (id,))
        rows=cursor.fetchall()
        for r in rows:
            employee=r
        if employee is not None:
            return jsonify(employee), 200
        else:
            return "Something wrong", 404
    
    if request.method=="PUT":
        try:
           
            sql=""" update employee set fname=?, lname=?, salary=? where id=?"""
            
            fname=request.form["fname"]
            lname=request.form["lname"]
            salary=request.form["salary"]
            
            updated_employee={
                "id" :id,
                "fname" :fname,
                "lname" :lname,
                "salary" :salary
              }
            conn.execute(sql,(fname,lname,salary,id))
            conn.commit()
            return updated_employee
        except Exception as e:
            return e
    
    if request.method=="DELETE":
        sql="""delete from employee where id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return "the employee with id: {} has been deleted.".format(id), 200
    
    

if __name__=="__main__":
    app.run(debug=True)