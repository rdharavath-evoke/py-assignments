from logging import debug
from flask import Flask
from flask import Flask, render_template

import sqlite3
from flask import g


app=Flask(__name__,template_folder='template')
DATABASE = 'employee.db'

def get_db():
    db = getattr(g, '_employee', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#app=Flask(__name__)
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_employee', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    cur = get_db().cursor()
    data=cur.execute('SELECT * FROM employee')
    for x in data:
        print(x)
    return {}


@app.route("/employee")
def table():
    return render_template("table.html")


if __name__=='__main__':
    app.run(debug=True)

