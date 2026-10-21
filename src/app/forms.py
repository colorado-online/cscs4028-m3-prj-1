'''
CSC 4028 - Software Security Testing
Student:
Description: Project 1 - HeartStitch
'''

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, DateField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    dob = DateField('DOB', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    pronouns = StringField('Pronouns', validators=[DataRequired()])
    bio = TextAreaField('Bio')
    interests = StringField('Interests')
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class LoginForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class ListUserForm(FlaskForm):
    id = StringField('Id')
    name = StringField('Name')
    email = EmailField('Email')
    age = IntegerField('Age')
    gender = StringField('Gender')
    pronouns = StringField('Pronouns')
    bio = TextAreaField('Bio')
    interests = StringField('Interests')
