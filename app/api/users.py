# app/api/users.py

# from flask import request, abort
# from bson import ObjectId
from app.services.database import insert_user, get_all_users, get_user_by_id, update_user, delete_user

def create_user():
    data = request.json

    if not data:
        return {"error": "No data provided"}, 400

    user_id = insert_user(data)
    return {"message": "User created successfully", "id": str(user_id)}, 201

def get_users():
    users = get_all_users()
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return users, 200

def get_user(user_id):
    if not ObjectId.is_valid(user_id):
        abort(400, description="Invalid ID format")

    user = get_user_by_id(ObjectId(user_id))
    if user:
        user["_id"] = str(user["_id"])
        return user, 200
    else:
        abort(404, description="User not found")

def update_user(user_id):
    if not ObjectId.is_valid(user_id):
        abort(400, description="Invalid ID format")

    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        abort(400, description="Missing 'name' or 'email' field")

    result = update_user(ObjectId(user_id), data)
    if result.matched_count == 0:
        abort(404, description="User not found")

    return {"message": "User updated successfully"}, 200

def delete_user(user_id):
    if not ObjectId.is_valid(user_id):
        abort(400, description="Invalid ID format")

    result = delete_user(ObjectId(user_id))
    if result.deleted_count == 0:
        abort(404, description="User not found")

    return {"message": "User deleted successfully"}, 200
