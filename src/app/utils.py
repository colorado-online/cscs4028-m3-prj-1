'''
CSC 4028 - Software Security Testing
Student:
Description: Project 1 - HeartStitch
'''

from app import app, db
from app.models import User
import bcrypt

# creates a user with (optional) defaults
def create_user(id, name='', email='', dob='1900-01-01', gender='', pronouns='', bio='', interests='', password=bcrypt.hashpw('12345678'.encode('utf-8'), bcrypt.gensalt())): 
    with app.app_context(): 
        user = User(
            id=id, 
            name=name, 
            email=email,
            dob=dob, 
            gender=gender, 
            pronouns=pronouns,
            bio=bio, 
            interests=interests, 
            password=password)          
        db.session.add(user)
        db.session.commit()

# deletes a user given their id
def delete_user(id): 
    with app.app_context(): 
        user = User.query.filter_by(id=id).one()
        db.session.delete(user)
        db.session.commit()

# retrieves a user given their id
def retrieve_user(id): 
    user = None
    with app.app_context(): 
        user = User.query.filter_by(id=id).one()
    return user

# returns true if a user is following another user
def is_following(follower_id, following_id):
    with app.app_context(): 
        follower = User.query.filter_by(id=follower_id).one()
        for other in follower.followed: 
            if other.id == following_id: 
                return True 
    return False

# have a user follows another user
def follow(follower_id, following_id):
    with app.app_context(): 
        if follower_id != following_id: 
            follower = User.query.filter_by(id=follower_id).one()
            following = User.query.filter_by(id=following_id).one()
            follower.followed.append(following)
            db.session.commit()

# have a user unfollows another user
def unfollow(follower_id, following_id):
    with app.app_context(): 
        if follower_id != following_id: 
            follower = User.query.filter_by(id=follower_id).one()
            following = User.query.filter_by(id=following_id).one()
            follower.followed.remove(following)
            db.session.commit()
