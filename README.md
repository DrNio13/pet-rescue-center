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

`capstone-collection.postman_collection.json` Postman tests for each role and success and error cases.


<!-- TODOs -->

<!-- Instructions are provided in README for setting up authentication so reviewers can test endpoints at live application endpoint -->


<!-- 
All required configuration settings are included in a bash file which export:

The Auth0 Domain Name
The JWT code signing secret
The Auth0 Client ID
 -->


<!-- API is hosted live via Heroku
URL is provided in project README
API can be accessed by URL and requires authentication -->

<!-- Secrets are stored as environment variables. -->


<!-- Motivation for project
Project dependencies, local development and hosting instructions,
Detailed instructions for scripts to install any project dependencies, and to run the development server.
Documentation of API behavior and RBAC controls
 -->