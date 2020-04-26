# pet-rescue-center

SPA platform in Python and Angular 9 for Udacity

# Description

Web application that lists pet ads for potential adoption.

# Back-End

Python 3.7

# Pip Dependencies

`pip install -r requirements.txt`

# Dependencies

Web application most important dependencies are:
Flask
Flask-SQLAlchemy
SQLAlchemy

# Running the web server

`export FLASK_APP=flaskr
export FLASK_ENV=development
flask run`

# Database

database_name = "petrescuecenter"

#  Roles and Permissions
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

# Structure

`frontend` : Includes the frontend part of the application in Ionic/Angular. Check it's README.md for further details.

# Testing

`backend` folder includes Postman tests for each role and success and error cases.
