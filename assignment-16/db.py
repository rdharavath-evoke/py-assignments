import sqlite3

conn=sqlite3.connect("employee.db")

cursor=conn.cursor()

sql_query=""" create table employee(id int primary key, fname text,lname text,salary real ) """
               
cursor.execute(sql_query)