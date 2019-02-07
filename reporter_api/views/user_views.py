from flask import Flask, json, jsonify, request, Blueprint, current_app as app
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)


from reporter_api.controllers.user_controllers import User_controller

auth = Blueprint("auth", __name__)
user_controller = User_controller()


@auth.route('/api/v2/auth/signup/', methods=['POST'])
@auth.route('/api/v2/auth/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    return user_controller.add_reporter(request_data)


@auth.route('/api/v2/auth/users/', methods=['GET'])
@auth.route('/api/v2/auth/users', methods=['GET'])
@jwt_required
def fetch_users():
    current_user = get_jwt_identity()
    isadmin = current_user["isadmin"]
    if isadmin is True:
        return user_controller.fetch_users()
    return jsonify({
        "error": "Only admins can see users"
    }),403


@auth.route('/api/v2/auth/login/', methods=['POST'])
@auth.route('/api/v2/auth/login', methods=['POST'])
def login():
    user_data = request.get_json()
    return user_controller.signin(user_data)


@auth.route('/api/v2/auth/users/<int:userid>/', methods=['GET'])
@auth.route('/api/v2/auth/users/<int:userid>', methods=['GET'])
def get_a_reporter(userid):
    return user_controller.fetch_user(userid)
