# pet-rescue-center

SPA platform in Python and Angular 9 for Udacity

Public url of backend https://pet-rescue-center.herokuapp.com/
Public url of the project https://pet-rescue-center.herokuapp-app.com/
Frontend in Ionic calls the API server without CORS issues

# Description

Web application that lists pet ads for potential adoption.

# Back-End

Python 3.7

# Virtual Env

`python3 -m venv venv;
. venv/bin/activate`

# Pip Dependencies

`pip3 install -r requirements.txt`

# Running the web server locally

Run the following commands to run it locally

`export DATABASE_URL="postgres://localhost:5432/petrescuecenter"`
`export AUTH0_DOMAIN="drnio13.eu.auth0.com"`
`export ALGORITHMS=['RS256']`
`export API_AUDIENCE='pets'`
`python3 manage.py db init`
`python3 manage.py db migrate`
`python3 manage.py db upgrade`
`python3 app.py`

There is a frontend project associated with this web server api. Git clone https://github.com/DrNio13/pet-rescue-center-app and follow it's README.md file.

# Dependencies

Web application most important dependencies are:
Flask
Flask-SQLAlchemy
SQLAlchemy

# Database

database_name = "petrescuecenter"

#  Roles and Permissions

`setup.sh` contains valid jwt tokens for each role

Guest Users     GET /pets
Customer        GET /pets and /pets-details  POST /enquiries
Moderator       All APIS except permissions to Delete 
Manager         All permissions granted


# Status Codes
All endpoints return the following status codes in its API:

Status  Code Description
200	    OK
201     CREATED
400     BAD REQUEST
403     FORBIDDEN
404     NOT FOUND
500     INTERNAL SERVER ERROR

# Testing

`capstone-collection.postman_collection.json` Postman tests for each role and success and error cases.

# API


<!-- Documentation of API behavior and RBAC controls -->