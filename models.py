import os
from sqlalchemy import Column, String, Boolean, Integer, create_engine
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
if not database_path:
    database_name = "petrescuecenter"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


# Customer can show interest for a Pet through Enquiry Model

class Enquiry(db.Model):
    __tablename__ = "enquiries"

    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"), primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        "customers.id"), primary_key=True)

    def __init__(self, pet_id, customer_id):
        self.pet_id = pet_id
        self.customer_id = customer_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def long_format(self):
        return {
            'pet_id': self.pet_id,
            'customer_id': self.customer_id
        }


# Pet Model

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


# Customer Model

class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    email = Column(String)

    def __init__(self, email):
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short_long(self):
        return {
            'id': self.id
        }

    def long_format(self):
        return {
            'id': self.id,
            'email': self.email
        }
