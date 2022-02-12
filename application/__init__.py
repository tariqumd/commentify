from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_login import LoginManager
from flask_login import UserMixin,logout_user,current_user,login_required,login_user
from datetime import date,datetime


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///commentify_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)
#login_manager=LoginManager(app)
#login_manager.init_app(app)
#login_manager.login_view='login'

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')

# Seeding database with manual data 
# @app.cli.command('db_seed')
# def db_seed():


#Database class
class users(db.Model):
    email_id=db.Column(db.String(60),primary_key=True,nullable=False)
    password=db.Column(db.String(90),nullable=False)
    secret_key=db.Column(db.String(60),nullable=False)

class comments(db.Model):
    comment_id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    email_id=db.Column(db.String(60),nullable=False)
    comment=db.Column(db.String(120),nullable=False)


from application import routes
if __name__=="__main__":
    app.run(debug=True)
