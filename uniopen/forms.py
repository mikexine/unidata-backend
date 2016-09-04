# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, PasswordField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(Form):
    username = TextField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    email = TextField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField(
                'Verify password',
                [DataRequired(), EqualTo('password', message='Passwords must match')])

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AddUniversityForm(Form):
    shortname = TextField('Short university name', validators=[DataRequired()])
    fullname = TextField('Full name', validators=[DataRequired()])
    address = TextField('Main address')


class AddStudyRoomForm(Form):
    shortname = TextField('Short name', validators=[DataRequired()])
    fullname = TextField('Full name', validators=[DataRequired()])
    seats = TextField('Number of seats')
    address = TextField('Main address')
    texthours = TextField('Opening hours')
    phone = TextField('Phone number')
