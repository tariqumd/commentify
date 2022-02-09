from application import app,db
from flask import render_template,request,json,Response, redirect , flash, url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import literal

@app.route("/")
@app.route("/index",methods=['GET','POST'])
def index():
    return render_template("index.html",index=True)

@app.route("/logout")
def logout():

    session['user']=""
    session['name']=""
    session['type']=False

    return redirect(url_for('index'))

@app.route("/signup",methods=['GET','POST'])
def signup():
    return render_template("signup.html",register_employee=True)

