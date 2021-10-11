import sqlite3

conn=sqlite3.connect("books.db")

cursor=conn.cursor()

sql_query=""" create table book(
               id integer primary key,
               auther text not null,
               language text not null,
               title text not null
               ) """
               
cursor.execute(sql_query)