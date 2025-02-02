# Flask_MongoDB_Application

This project is a simple Flask API that interacts with a MongoDB database to perform CRUD (Create, Read, Update, Delete) operations on user data. Both the Flask application and MongoDB are containerized using Docker, making it easy to set up and run the project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

Access the Application
Flask API: The API will be available at http://localhost:5000.

MongoDB: The database will be available at mongodb://root:example@localhost:27017

# API Endpoints

1️. **POST /users**
   - Stores data in MongoDB.
   - Send a JSON payload in the request body.
   - Example request:
     {
  "name": "Aarav Patel",
  "email": "aarav.patel@example.com"
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
    "_id": "<user_id>",
    "name": "Aarav Patel",
    "email": "aarav.patel@example.com"
        }
     ]

3️. **GET /users/<id>**
   - Fetches a single user by their MongoDB Object ID.
   - If the ID is invalid or not found, it returns an error.
   - Example response:
     {
  "_id": "<user_id>",
  "name": "Aarav Patel",
  "email": "aarav.patel@example.com"
   }

4️. **PUT /users/<id>**
   - Updates a user’s `name` and `email` by their ID.
   - Requires a JSON body with `name` and `email` fields.
   - Example request:
     {
  "name": "Aarav Singh",
  "email": "aarav.singh@example.com"
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
