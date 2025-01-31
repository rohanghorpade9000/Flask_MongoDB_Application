from flask import Flask, request, abort
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

#MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["corider_db"]
collection = db["users"]


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json

    if not data:
        return {"error": "No data provided"}

    inserted_id = collection.insert_one(data).inserted_id
    return {"message": "Data stored successfully", "id": str(inserted_id)}, 201


@app.route("/users", methods=["GET"])
def get_users():

    users = []

    for user in collection.find():
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        users.append(user)

    for user in users:
        user["_id"] = str(user["_id"])

    return users, 200

@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    if not ObjectId.is_valid(id):
        abort(400, description="Invalid ID format")

    user = collection.find_one({"_id": ObjectId(id)}, {"_id": 1, "name": 1, "email": 1})

    if user:
        user["_id"] = str(user["_id"])
        return user, 200
    else:
        abort(404, description="User not found")


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    if not ObjectId.is_valid(id):
        abort(400, description="Invalid ID format")

    data = request.get_json()

    if not data.get("name") or not data.get("email"):
        abort(400, description="Missing 'name' or 'email' field")

    result = collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": data["name"], "email": data["email"]}}
    )

    if result.matched_count == 0:
        abort(404, description="User not found")

    return {"message": "User updated successfully"}, 200


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    if not ObjectId.is_valid(id):
        abort(400, description="Invalid ID format")

    result = collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        abort(404, description="User not found")

    return {"message": "User deleted successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True)
