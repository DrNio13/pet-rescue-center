import os
from sqlalchemy import Column, String, Boolean, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "petrescuecenter"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Enquiry(db.Model):
    __tablename__ = "enquiries"

    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"), primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        "customers.id"), primary_key=True)

    def __init__(self, pet_id, customer_id):
        self.pet_id = pet_id
        self.customer_id = customer_id

    def long_format(self):
        return {
            'pet_id': self.pet_id,
            'customer_id': self.customer_id
        }


class Pet(db.Model):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    description = Column(String)
    seeking_owner = Column(Boolean)

    def __init__(self, name, breed, description, seeking_owner):
        self.name = name
        self.breed = breed
        self.description = description
        self.seeking_owner = seeking_owner

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short_format(self):
        return {
            'id': self.id,
            'name': self.name,
            'seeking_owner': self.seeking_owner
        }

    def long_format(self):
        return {
            'id': self.id,
            'name': self.name,
            'breed': self.breed,
            'description': self.description,
            'seeking_owner': self.seeking_owner
        }


class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short_format(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }

    def format_long(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email
        }


class Manager(db.Model):
    __tablename__ = 'managers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    def __init__(self, name, surname, seeking_pet):
        self.name = name
        self.surname = surname

    def long_format(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }
