import os
import re
import urllib.request
from flask import *
import sqlite3
from werkzeug.utils import secure_filename
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "secret key"

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/logon')
def logon():
	return render_template('signup.html')
@app.route("/signup",methods=["post","get"])
def signup():
    username =request.form['user']
    name = request.form['name']
    email = request.form['email']
    number = request.form["mobile"]
    password = request.form['password']
    role="student"
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`,'role') VALUES (?, ?, ?, ?, ?,?)",(username,email,password,number,name,role))
    con.commit()
    con.close()
    return render_template("index.html")
@app.route("/signin",methods=["post"])
def signin():
    mail1 = request.form['user']
    password1 = request.form['password']
    con = sqlite3.connect('signup.db')
    data=0
    data =con.execute("select `user`, `password`,role from info where `user` = ? AND `password` = ?",(mail1,password1,)).fetchall()  
    print(data)
    if mail1 == 'admin' and password1 == 'admin':
        session['username'] ="admin"
        return redirect("myful")
    elif mail1 == str(data[0][0]) and password1 == str(data[0][1]):
        print(data)
        session['username'] =data[0][0]
        return redirect("myful")
    else:
        return render_template("signup.html")
@app.route("/myful")
def myful():
     return render_template("student.html")



@app.route('/logout')
def home():
    session.pop('username', None)
    return render_template("index.html")
   
if __name__ == '__main__':
    app.run(debug=True)
