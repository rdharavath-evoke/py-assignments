from logging import debug
from flask import Flask, render_template, request, redirect
import sqlite3
from flask import g


app=Flask(__name__,template_folder='template')
DATABASE = 'employee.db'

def get_db():
    db = getattr(g, '_employee', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_employee', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
   return render_template('home.html')

@app.route("/employee", methods=['GET'])
def employee():
    con = get_db()
    cur=con.cursor()
    cur.execute('SELECT * FROM employee')
    data=cur.fetchall()
    return render_template("employee.html", data=data)



@app.route('/enternew')
def enternew():
    return render_template('employee2.html')

#****************************************************************            

@app.route('/employeeupdate')
def employeeupdate():
    emp_id=request.args.get("id")
    cur = get_db().cursor()
    cur.execute(f"SELECT * FROM employee where id={emp_id}")
    data=cur.fetchall()
    if len(data)!=0:
        return render_template('update.html',data=data[0])
    return render_template('update.html',msg="Id not found",data=False)



@app.route("/updates",methods = ['POST'])
def updates():
    try:
        id = request.form['id']
        nm = request.form['nm']
        salary = request.form['salary']
        email = request.form['email']
            #course = request.form['course']

        con = get_db()
        cursor = con.cursor()

        sqlite_update_query = """Update employee set name=?, salary = ?, email = ? where id = ?"""
        columnValues = (nm,salary, email, id)
        cursor.execute(sqlite_update_query, columnValues)
        con.commit()
        msg="Multiple columns updated successfully"

    except sqlite3.Error as error:
        msg="Failed to update multiple columns of sqlite table"+str(error)
    finally:
        return render_template("result.html",msg = msg)


@app.route("/deleteemployee",methods=["GET"])
def deletemployee():
    empid=request.args.get("id")
    con = get_db()
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM employee where id={empid}")
    con.commit()
    return redirect("/employee")




if __name__=='__main__':
    app.run(debug=True)

