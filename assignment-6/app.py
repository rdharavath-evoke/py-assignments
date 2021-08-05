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

@app.route('/home')
def home():
   return render_template('home.html')

@app.route("/employee")
def employee():
    con = get_db()
    cur=con.cursor()
    cur.execute('SELECT * FROM employee')
    data=cur.fetchall()
    return render_template("employee.html", data=data)


@app.route("/employee3")
def employee_updation():
    con = get_db()
    cur=con.cursor()
    cur.execute('SELECT * FROM employee')
    data=cur.fetchall()
    return render_template("update.html", data=data)

#app=Flask(__name__,template_folder='template2')
@app.route('/enternew')
def enternew():
    return render_template('employee2.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == "POST":
        try:
            id = request.form['id']
            nm = request.form['nm']
            salary = request.form['salary']
            #email = request.form['email']
            #course = request.form['course']

            con=get_db()
            cur = con.cursor()
            cur.execute(f'SELECT * FROM employee WHERE Id={id}')
            data=cur.fetchall()
            if len(data)==0:
                cur.execute("INSERT INTO employee (Id,Name,Salary) VALUES (?,?,?)",(id,nm,salary) )
                con.commit()
                msg = "Record successfully added"
            else:
                msg="id already exist"
        except Exception as emp: 
            #con.rollback()
            msg = "error in insert operation "+str(emp)
      
        finally:
            return render_template("result.html",msg = msg)
            con.close()


#****************************************************************#            

@app.route('/employee=update-here')
def update():
    return render_template('update.html')


@app.route("/updates",methods = ['POST', 'GET'])
def updates():
    if request.method == "POST":
        try:
            id = request.form['id']
            #nm = request.form['nm']
            salary = request.form['salary']
            email = request.form['email']
            #course = request.form['course']

            con = get_db()
            cursor = con.cursor()

            sqlite_update_query = """Update employee set salary = ?, email = ? where id = ?"""
            columnValues = (salary, email, id)
            cursor.execute(sqlite_update_query, columnValues)
            con.commit()
            msg="Multiple columns updated successfully"

        except sqlite3.Error as error:
            msg="Failed to update multiple columns of sqlite table"+str(error)
        finally:
            return render_template("result.html",msg = msg)
#updateMultipleColumns(3, 6500, 'ben_stokes@gmail.com')




app.route('/header')
def head():
    con = get_db()
    cur=con.cursor()
    cur.execute("select count(*) from employee")
    number_of_employees = cur.fetchone()[0]
    return render_template('header.html', number_of_employees=number_of_employees)



if __name__=='__main__':
    app.run(debug=True)

