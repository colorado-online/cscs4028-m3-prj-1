'''
CSC 4028 - Software Security Testing
Student:
Description: Project 1 - HeartStitch
'''

from app import db 
from flask_login import UserMixin
from datetime import datetime

followers = db.Table(
    'followers',
    db.Column('follower_id', db.String, db.ForeignKey('users.id'), primary_key=True),
    db.Column('followed_id', db.String, db.ForeignKey('users.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    dob = db.Column(db.String)
    gender = db.Column(db.String)
    pronouns = db.Column(db.String)
    bio = db.Column(db.String)
    interests = db.Column(db.String)
    password = db.Column(db.LargeBinary)

    # Users that this user is following
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        back_populates='followers', lazy='joined'
    )

    # Users that are following this user
    followers = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.followed_id == id),
        secondaryjoin=(followers.c.follower_id == id),
        back_populates='followed', lazy='joined'
    )

    def age(self):
        dob = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
