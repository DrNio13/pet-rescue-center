import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc, text
import json
from flask_cors import CORS

from models import setup_db, Pet, Enquiry, Customer, db
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


# HealthCheck Route

@app.route("/")
def health_check():
    return jsonify({
        "healthy": True
    })


# Pets Routes

@app.route("/pets")
def get_pets():
    try:
        pets = Pet.query.all()
        pets_formatted = [pet.short_format() for pet in pets]

        return jsonify(pets_formatted)
    except Exception as e:
        print(e)
        abort(500)


@app.route("/pets-details")
@requires_auth('get:pets-details')
def get_pets_detail(jwt):
    try:
        pets = Pet.query.all()
        pets_formatted = [pet.long_format() for pet in pets]

        return jsonify(pets_formatted)
    except Exception as e:
        print(e)
        abort(500)


@app.route("/pets/<int:id>")
@requires_auth('get:pets')
def get_pet_by_id(jwt, id):
    if id is None or id <= 0:
        return json.dumps({
            'success':
                False,
                'error':
                'Invalid id #' + str(id)
        }), 404

    pet = Pet.query.filter(Pet.id == id).one_or_none()
    if (pet is None):
        return json.dumps({
            'success':
                False,
                'error':
                'Pet #' + str(id) + ' not found to be edited'
        }), 404

    return jsonify(pet.long_format())


@app.route("/pets", methods=["POST"])
@requires_auth('post:pets')
def create_pet(jwt):
    body = request.get_json()

    name = body.get("name", None)
    breed = body.get("breed", None)
    seeking_owner = body.get("seeking_owner", None)
    description = body.get("description", None)

    if (name is None or breed is None or seeking_owner is None or description is None):
        return json.dumps({
            'success':
                False,
                'error':
                'Bad request'
        }), 400

    pet = Pet(name=name, breed=breed,
              seeking_owner=seeking_owner, description=description)
    pet.insert()

    return jsonify(pet.long_format())


@app.route("/pets/<int:id>", methods=["PATCH"])
@requires_auth('patch:pets')
def update_pet(jwt, id):
    if id is None or id <= 0:
        return json.dumps({
            'success':
                False,
                'error':
                'Invalid id #' + str(id)
        }), 404

    body = request.get_json()
    description = ''
    seeking_owner = ''
    try:
        description = body.get("description")
        seeking_owner = body.get("seeking_owner")
    except:
        return json.dumps({
            'success':
                False,
                'error':
                'Missing required fields'
        }), 400
    else:
        pet = Pet.query.filter(Pet.id == id).one_or_none()
        if (pet is None):
            return json.dumps({
                'success':
                    False,
                    'error':
                    'Pet #' + str(id) + ' not found to be edited'
            }), 404

        pet.description = description
        pet.seeking_owner = seeking_owner
        pet.update()

        return jsonify(pet.long_format())


@app.route("/pets/<int:id>", methods=["DELETE"])
@requires_auth('delete:pets')
def delete_pet_by_id(jwt, id):
    if id is None or id <= 0:
        return json.dumps({
            'success':
                False,
                'error':
                'Invalid id #' + str(id)
        }), 404

    pet = Pet.query.filter(Pet.id == id).one_or_none()
    if (pet is None):
        return json.dumps({
            'success':
                False,
                'error':
                'Pet #' + str(id) + ' not found to be deleted'
        }), 404

    pet.delete()

    return jsonify({
        "success": True,
        "delete": pet.id
    })


# Enquiries Routes

@app.route("/enquiries")
@requires_auth('get:enquiries')
def get_enquiries(jwt):
    enquiries = Enquiry.query.all()
    formatted_enquiries = [enquiry.long_format() for enquiry in enquiries]

    return jsonify(formatted_enquiries)


@app.route("/enquiries/<int:id>")
@requires_auth('get:enquiries')
def get_enquiry_by_id(jwt, id):
    enquiry = Enquiry.query.filter(Enquiry.pet_id == id).one_or_none()
    if (enquiry is None):
        return json.dumps({
            'success':
                False,
                'error':
                'Enquiry #' + str(id) + ' not found'
        }), 404

    formatted_enquiry = enquiry.long_format()

    return jsonify(formatted_enquiry)


@app.route("/enquiries", methods=["POST"])
@requires_auth('post:enquiries')
def create_enquiry(jwt):
    try:
        body = request.get_json()
        pet_id = body.get("id", None)
        customer_email = body.get("email", None)

        if (id is None or customer_email is None):
            return json.dumps({
                'success':
                False,
                'error':
                'Bad request'
            }), 400

        pet = Pet.query.filter(Pet.id == pet_id).one_or_none()
        if (pet is None):
            return json.dumps({
                'success':
                False,
                'error':
                    'Pet #' + str(id) + ' not found'
            }), 404

        customer = Customer.query.filter(
            Customer.email == customer_email).one_or_none()
        if (customer is None):
            customer = Customer(email=customer_email)
            customer.insert()

        enquiry = Enquiry(pet_id=pet_id, customer_id=customer.id)
        enquiry.insert()

        return jsonify(enquiry.long_format())
    except Exception as e:
        print(e)
        abort(500)


# Customers Routes

@app.route("/customers")
@requires_auth('get:customers')
def get_customers(jwt):
    customers = Customer.query.all()
    formatted_customers = [customer.long_format() for customer in customers]

    return jsonify(formatted_customers)


@app.route("/customers/<int:id>")
@requires_auth('get:customers')
def get_customer_by_id(jwt, id):
    customer = Customer.query.filter(Customer.id == id).one_or_none()
    if (customer is None):
        return json.dumps({
            'success':
                False,
                'error':
                    'Customer #' + str(id) + ' not found'
        }), 404

    formatted_customer = customer.long_format()

    return jsonify(formatted_customer)


# Error Handling

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "It's not you, it's us"
    }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Sorry, we couldn't find what you were looking for"
    }), 404


@app.errorhandler(AuthError)
def handle_auth_error(exception):
    response = jsonify(exception.error)
    response.status_code = exception.status_code

    return response
