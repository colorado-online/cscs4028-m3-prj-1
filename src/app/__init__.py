'''
CSC 4028 - Software Security Testing
Student:
Description: Project 1 - HeartStitch
'''

from flask import Flask
import os

app = Flask(
    __name__, 
    template_folder=os.path.join(os.getcwd(), 'templates'), 
    static_folder=os.path.join(os.getcwd(), 'static'))

# consider using an ENVIRONMENT VARIABLE to improve security
app.secret_key = 'you-will-never-guess'

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

# db from models
from app import models
with app.app_context():
    db.create_all()

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User

# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from app import routes
  