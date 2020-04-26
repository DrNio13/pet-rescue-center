import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import setup_db, Pet, Enquiry, Customer, Manager
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


# ROUTES

@app.route("/")
def health_check():
    return jsonify({
        "healthy": True
    })


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


@app.route("/pets", methods=["POST"])
@requires_auth('post:pets')
def create_pet(jwt):
    try:
        body = request.get_json()

        name = body.get("name", None)
        breed = body.get("breed", None)
        seeking_owner = body.get("seeking_owner", None)
        description = body.get("description", None)

        if (name is None or breed is None or seeking_owner is None or description is None):
            abort(400)

        pet = Pet(name=name, breed=breed,
                  seeking_owner=seeking_owner, description=description)
        pet.insert()

        return jsonify(pet.long_format())
    except:
        abort(500)


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
    description = body.get("description")
    seeking_owner = body.get("seeking_owner")

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
                'Pet #' + str(id) + ' not found to be edited'
        }), 404

    pet.delete()

    return jsonify({
        "success": True,
        "delete": pet.id
    })


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
