
from logging import debug
from flask import Flask,request,jsonify,redirect,url_for,flash
import json
import os
import sqlite3
from flask_cors import CORS, cross_origin
from werkzeug.datastructures import FileMultiDict
from werkzeug.utils import format_string, secure_filename
from flask import send_file, send_from_directory



app=Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.secret_key="caircocoders-ednalan"

UPLOAD_FOLDER="D:/images"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16*1024*1024

ALLOWED_EXTENTIONS = set(['txt','pdf','png', 'jpg', 'jpeg', 'gif', 'mp4'])

def allowed_file(filename):
    return "." in filename and filename.rsplit('.',1)[1].lower in ALLOWED_EXTENTIONS

def db_connection():
    conn=None
    try:
        conn=sqlite3.connect('books.db')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/loadimage/<filename>")
def sendfile(filename):
    return send_from_directory(UPLOAD_FOLDER, f"{filename}.jpg")

@app.route("/loadvideo/<filename>")
def display_video(filename):
    return send_from_directory(UPLOAD_FOLDER, f"{filename}.mp4")
    

@app.route("/books",methods=["GET","POST"])
@cross_origin()
def books():
    conn=db_connection()
    cursor=conn.cursor()
    
    if request.method=="GET":
        cursor=conn.execute("select * from book")
        books=[
            dict(id=row[0], auther=row[1], language=row[2], title=row[3], data=row[4])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        
    
    
    if request.method=="POST":
        try:
            
            print('....')
            file = request.files['file'] if request.files.get('file') else None
            print('....')
            print (file)
            
           
            new_auther=request.form["auther"]
            new_lang=request.form["language"]
            new_title=request.form["title"] 
            # new_id=request.form["id"]
            
            sql=""" insert into book (auther, language, title) values(?,?,?)"""
            
            curser=cursor.execute(sql,(new_auther,new_lang,new_title)) 
            conn.commit()
            
            
            if file : 
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],f"{cursor.lastrowid}.jpg"))
            
            # return f"Book with the id : {curser.lastrowid} created successfully",201  
            
            if file : 
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],f"{cursor.lastrowid}.mp4"))
            
            return f"Book with the id : {curser.lastrowid} created successfully",201 
        
        except Exception as e: 
            return str(e)


@app.route("/books/<int:id>", methods=["GET","PUT","DELETE"])
@cross_origin()
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
        try:
            
            print('....')
            file = request.files['file'] if request.files.get('file') else None
            print('....')
            print (file)
            
            
            
            sql=""" update book set title=?, auther=?, language=?, data=? where id=?"""
            
            # req_data =  request.get_json(force=True)
            auther=request.form["auther"]
            language=request.form["language"]
            title=request.form["title"]
            # data=req_data["data"]
            
            updated_book={
                "id":id,
                "auther": auther,
                "language":language,
                "title":title,
            
            }
            conn.execute(sql,(title,auther,language,id))
            conn.commit()
            
            if file :
                
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],f"{cursor.lastrowid}.jpg"))
            
            return updated_book
        except Exception as e:
            return e
    
    if request.method=="DELETE":
        sql="""delete from book where id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return "the book with id: {} has been deleted.".format(id), 200
    
    
       
@app.route('/pagination/page/<int:pages>/limit/<int:limit>')
@cross_origin()
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

    