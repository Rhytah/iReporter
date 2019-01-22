from flask import Flask, json, jsonify, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from reporter_api import app
from reporter_api.controllers.user_controllers import User_controller

user_controller = User_controller()


@app.route('/api/v1/auth/signup/', methods=['POST'])
def signup():
    request_data = request.get_json()
    return user_controller.add_reporter(request_data)


@app.route('/api/v1/auth/users/', methods=['GET'])
@jwt_required
def fetch_users():
    current_user = get_jwt_identity()
    isadmin = current_user.get("isadmin")
    if isadmin is True:
        return user_controller.fetch_reporters()
    return jsonify({
        "status": 401,
        "error": "Only admins can see users"
    })


@app.route('/api/v1/auth/login/', methods=['POST'])
def login():
    user_data = request.get_json()
    return user_controller.signin(user_data)


@app.route('/api/v1/auth/users/<int:user_id>/', methods=['GET'])
def get_a_reporter(user_id):
    return user_controller.fetch_reporter(user_id)
