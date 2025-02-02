#from flask import Flask
from app.api.users import create_user, get_users, get_user, update_user, delete_user

app = Flask(__name__)

# Register API routes
app.route('/users', methods=['POST'])(create_user)
app.route('/users', methods=['GET'])(get_users)
app.route('/users/<user_id>', methods=['GET'])(get_user)
app.route('/users/<user_id>', methods=['PUT'])(update_user)
app.route('/users/<user_id>', methods=['DELETE'])(delete_user)
