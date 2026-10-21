'''
CSC 4028 - Software Security Testing
Student:
Description: Project 1 - HeartStitch
'''

from app import app
# from app import limiter
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from app.models import User
from app.forms import SignUpForm, LoginForm, ListUserForm
import bcrypt
# import requests
from app.utils import *

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.password.data == form.password_confirm.data:
            hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            try: 
                create_user(
                    form.id.data,
                    name=form.name.data, 
                    email=form.email.data,
                    dob=form.dob.data, 
                    gender=form.gender.data, 
                    pronouns=form.pronouns.data,
                    bio=form.bio.data, 
                    interests=form.interests.data, 
                    password=hashed_password
                )
            except Exception as ex: 
                return f'<p>There was an error creating the user: {ex}</p>' 
            return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try: 
            user = retrieve_user(form.id.data)
            if user and bcrypt.checkpw(form.password.data.encode(), user.password):
                login_user(user)
                return redirect(url_for('list_users'))
        except Exception as ex: 
            return f'<p>There was an error retrieving the user: {ex}</p>'
    return render_template('login.html', form=form)

@app.route('/users')
def list_users():
    try: 
        # TODO: add a filter so the current user is not displayed
        # TODO: sort users by id
        users = User.query.all()
        return render_template('list_users.html', current_user=current_user, users=users)
    except Exception as ex: 
        return f'<p>There was an error listing users: {ex}</p>'
    
@app.route('/users/<id>')
def list_user(id):
    form = ListUserForm()
    try: 
        user = retrieve_user(id)
        form.id.data = user.id 
        form.name.data = user.name 
        form.email.data = user.email
        form.age.data = user.age()
        form.gender.data = user.gender 
        form.pronouns.data = user.pronouns 
        form.bio.data = user.bio 
        form.interests.data = user.interests
        follower = is_following(current_user.id, user.id)
    except: 
        pass
    return render_template('user.html', form=form, current_user=current_user, user=user, follower=follower)

@app.route('/users/<id>/follow')
def follow_user(id):
    try: 
        follow(current_user.id, id) 
        return redirect(url_for('list_user', id=id))
    except Exception as ex: 
        return f'<p>There was an error following user {id}: {ex}</p>'
    
@app.route('/users/<id>/unfollow')
def unfollow_user(id):
    try: 
        unfollow(current_user.id, id) 
        return redirect(url_for('list_user', id=id))
    except Exception as ex: 
        return f'<p>There was an error unfollowing user {id}: {ex}</p>'

@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/users/delete', methods=['GET', 'POST'])
def delete():
    id = current_user.id
    delete_user(current_user.id)
    logout_user()
    return redirect(url_for('index'))
