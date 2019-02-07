from reporter_api.models.user_model import User
from flask import jsonify, json, request, current_app as app

from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from reporter_api.utilities.user_validators import UserValidator
import datetime

validator = UserValidator()
user_obj = User()
JWT_ACCESS_TOKEN_EXPIRES = False


class User_controller:

    def add_reporter(self, *args):
        user_data = request.get_json()
        firstname = user_data.get('firstname')
        lastname = user_data.get('lastname')
        email = user_data.get('email')
        username = user_data.get('username')
        password = user_data.get('password')
        invalid_user = validator.validate_add_user(
            firstname, lastname, username, email, password)
        if invalid_user:
            return invalid_user
        existent_reporter = user_obj.signup_search_user(email)

        if existent_reporter:
            return existent_reporter
        new_user = user_obj.create_user(
            firstname, lastname, username, password, email)

        return jsonify({"data": {
            "user": new_user,
            "message": "signup successful"}
        }), 201

    def signin(self, args):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username:
            return jsonify({"error": "Provide Valid username"}), 400

        if not password:
            return jsonify({"error": "Provide password"}), 400

        returned_user = user_obj.login_search_user(username)
        print(returned_user)
        if returned_user is None:
            return jsonify({
                "error": 'A user with this email and password was not found.'
            }),401
        if username == returned_user.get('username') and password == returned_user.get('password'):
            token_expiry = datetime.timedelta(days=1)
            user_identity = dict(
                userid=returned_user.get('userid'),
                isadmin=returned_user.get('isadmin')
            )

            token = create_access_token(
                identity=user_identity, expires_delta=token_expiry)
            return jsonify({
                'token': token,
                'message': 'You have successfully logged in',
                'isadmin': returned_user['isadmin'],
                'username': returned_user['username'],
            })

        return jsonify({
            'error': "invalid credentials. \
            Use a registered email and password",
        }), 401

    def fetch_users(self):
        result = user_obj.get_users()
        if result:
            return jsonify({

                "data": result,
                "message": "You are viewing registered reporters"})

    def fetch_user(self, userid):
        user = user_obj.get_user(userid)
        if user:
            return jsonify({
                "data": user,
                "message": "User details displayed"
            })
        return jsonify({

            "error": "user_id out of range, try again with a valid id"
        }), 404
