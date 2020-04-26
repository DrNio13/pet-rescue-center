# Back-End

Python 3.7

# Pip Dependencies

`pip install -r requirements.txt`

# Running the server

`export FLASK_APP=flaskr
export FLASK_ENV=development
flask run`

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