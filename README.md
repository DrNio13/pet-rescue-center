# pet-rescue-center

SPA platform in Python and Angular 9 for Udacity

Public url of backend https://pet-rescue-center.herokuapp.com/

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

<!-- === pet-rescue-center Config Vars
DATABASE_URL:                 postgres://xeimsecbizfcbx:ea5487c7391f48b915c3b916fa9f124188484179e0d34f92f826ce8da6a43181@ec2-34-234-228-127.compute-1.amazonaws.com:5432/d506arn7mg9ade

HEROKU_POSTGRESQL_ORANGE_URL: postgres://vhttpwwrwmvdnq:430bbb606e95e0981fb0efe72ce42b5c547968c5db86cf42cc7b7be5eed0bdf4@ec2-34-234-228-127.compute-1.amazonaws.com:5432/d58umm2b6bq8gp -->


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