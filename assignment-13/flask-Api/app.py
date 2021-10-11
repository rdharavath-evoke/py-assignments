from logging import debug
from flask import Flask,request,jsonify
import json
import sqlite3
from flask_cors import CORS, cross_origin

from flask import Blueprint
from flask_paginate import Pagination
# from flask_paginate import Pagination, get_page_parameter

app=Flask(__name__)
cors = CORS(app)

def db_connection():
    conn=None
    try:
        conn=sqlite3.connect('books.db')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/books",methods=["GET","POST"])
@cross_origin()
def books():
    conn=db_connection()
    cursor=conn.cursor()
    
    if request.method=="GET":
        cursor=conn.execute("select * from book")
        books=[
            dict(id=row[0], auther=row[1], language=row[2], title=row[3])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        
    
    if request.method=="POST":
        new_auther=request.form["auther"]
        new_lang=request.form["language"]
        new_title=request.form["title"] 
        new_id=request.form["id"]
        sql=""" insert into book (auther, language, title, id) values(?,?,?,?)"""
        curser=cursor.execute(sql,(new_auther,new_lang,new_title,new_id)) 
        conn.commit()
        return f"Book with the id : {curser.lastrowid} created successfully",201  

@app.route("/book/<int:id>", methods=["GET","PUT","DELETE"])
def single_book(id):
    conn=db_connection()
    cursor=conn.cursor()
    book=None
    if request.method=="GET":
        cursor.execute("select * from book where id=?", (id,))
        rows=cursor.fetchall()
        for r in rows:
            book=r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404
    
    if request.method=="PUT":
        sql=""" update book set title=?, auther=?, language=? where id=?"""
        auther=request.form["auther"]
        language=request.form["language"]
        title=request.form["title"]
        
        updated_book={
            "id":id,
            "auther": auther,
            "language":language,
            "title":title
        }
        conn.execute(sql,(auther,language,title,id))
        conn.commit()
        return jsonify(updated_book)
    
    if request.method=="DELETE":
        sql="""delete from book where id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return "the book with id: {} has been deleted.".format(id), 200
    
    
@app.route('/pagination/page/<int:pages>/limit/<int:limit>')
def pagination(pages,limit):

    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("select count(*) from book")
    count=cursor.fetchone()[0]
    cursor.execute("select * from book")
    totalpages=int(count/limit)
    start = (pages - 1) * limit
    end = pages * limit if count > pages * limit else count
    if count:
        books=[{"total records":count,"total pages":totalpages,"start":start,"end":end-1,"data":
                [dict(id=row[0], auther=row[1], language=row[2], title=row[3])
                for row in cursor.fetchall()[start:end]]}
        ]
        
    if books is not None:
        return jsonify(books)
        
    
if __name__=="__main__":
    app.run(debug=True)

    