# -*- coding: utf-8 -*-

"""
UniOpen models.
"""
from .app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User "{username}">'.format(username=self.username)

class University(db.Model):

    __tablename__ = 'university'

    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, shortname=None, fullname=None):
        self.shortname = shortname
        self.fullname = fullname

    def __repr__(self):
        return '<Uni "{shortname}">'.format(shortname=self.shortname)

db.create_all()
