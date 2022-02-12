from application import app,db,users
from flask import render_template,request,json,Response, redirect , flash, url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import literal

@app.route("/")
@app.route("/index",methods=['GET','POST'])
def index():

    if request.method == "POST":
        user=users.query.filter_by(email_id=request.form.get("email")).first()
        if user and check_password_hash(user.password,request.form.get("password")):
                session['user']=user.email_id
                session['status']="logged_in"
                flash(f"{user.email_id} Logged In","success")
                return redirect("home")
        else:
            flash("Invalid Credentials","danger")
            return redirect("index")

    return render_template("index.html",index=True)

@app.route("/signup",methods=['GET','POST'])
def signup():

    if request.method=="POST":
        email_check=users.query.filter_by(email_id=request.form.get("email")).scalar()
        # Checks whether username is already available
        if email_check == None:
            db.session.add_all([
                            users(email_id=request.form.get("email"),password=generate_password_hash(request.form.get('password')),
                                    secret_key=request.form.get('seckey'))])
            db.session.commit()
            flash("Signup successfull","success")
            return redirect("index")

        else:
            flash("Email id already present !","warning")
            return redirect("signup")

    return render_template("signup.html",signup=True)

@app.route("/home",methods=['GET','POST'])
def home():

    return render_template("home.html",home=True)

@app.route("/logout")
def logout():

    session['user']=""
    session['status']="logged_out"
    flash("Logged Out","success")
    return redirect(url_for('index'))