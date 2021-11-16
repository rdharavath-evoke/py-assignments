import sqlite3

conn=sqlite3.connect("books.db")

cursor=conn.cursor()

sql_query=""" ALTER TABLE book
drop column data """
               
cursor.execute(sql_query)