# Flask_MongoDB_Application

This is a simple Flask application that interacts with a MongoDB database to perform CRUD (Create, Read, Update, Delete) operations on user data. The application is containerized using Docker, and the MongoDB instance is also run as a Docker container.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

1) Start the MongoDB Container

The application uses MongoDB as its database. You can start the MongoDB container using Docker Compose:

docker-compose up -d

2) Run the Flask Application

python main.py

3) Stopping the Application

# API Endpoints

1️. **POST /users**
   - Stores data in MongoDB.
   - Send a JSON payload in the request body.
   - Example request:
     {
       "name": "John Doe",
       "email": "john@example.com"
     }
   - Response:
     {
       "message": "Data stored successfully",
       "id": "652d9f0b0c1e4b2f5b1a2c3d"
     }

2️. **GET /users**
   - Fetches all users from the database.
   - Returns a list of users with their `id`, `name`, and `email`.
   - Response:
     [
       {
         "_id": "652d9f0b0c1e4b2f5b1a2c3d",
         "name": "John Doe",
         "email": "john@example.com"
       }
     ]

3️. **GET /users/<id>**
   - Fetches a single user by their MongoDB Object ID.
   - If the ID is invalid or not found, it returns an error.
   - Example response:
     {
       "_id": "652d9f0b0c1e4b2f5b1a2c3d",
       "name": "John Doe",
       "email": "john@example.com"
     }

4️. **PUT /users/<id>**
   - Updates a user’s `name` and `email` by their ID.
   - Requires a JSON body with `name` and `email` fields.
   - Example request:
     {
       "name": "John Smith",
       "email": "johnsmith@example.com"
     }
   - Response:
     {
       "message": "User updated successfully"
     }

5️. **DELETE /users/<id>**
   - Deletes a user from the database using their ID.
   - Response:
     {
       "message": "User deleted successfully"
     }
