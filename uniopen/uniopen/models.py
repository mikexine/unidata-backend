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

    __tablename__ = 'universities'

    id = db.Column('universities_id', db.Integer, primary_key=True)
    shortname = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String, default="")
    studyrooms = db.relationship("Studyroom", backref="university", lazy='dynamic')

    def __init__(self, shortname=None, fullname=None, address=None,
                 studyroom=None):
        self.shortname = shortname
        self.fullname = fullname
        self.address = address
        self.studyroom = studyroom

    def __repr__(self):
        return '<Uni "{shortname}">'.format(shortname=self.shortname)


class Studyroom(db.Model):
    __tablename__ = 'studyroom'

    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String, default="")
    fullname = db.Column(db.String, default="")
    seats = db.Column(db.Integer)
    address = db.Column(db.String, default="")
    texthours = db.Column(db.String, default="")
    phone = db.Column(db.String, default="")
    university_id = db.Column(db.Integer, db.ForeignKey('universities.universities_id'))
    University = db.relationship('University')

    def __init__(self, shortname, fullname, seats, address, texthours, phone):
        self.shortname = shortname
        self.fullname = fullname
        self.seats = seats
        self.address = address
        self.texthours = texthours
        self.phone = phone




db.create_all()
