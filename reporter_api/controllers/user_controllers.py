from reporter_api.models.user_model import User
from flask import jsonify, json, request,current_app as app

from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from reporter_api.utilities.user_validators import UserValidator
import datetime

validator = UserValidator()
user_obj = User()

class User_controller:
      
    def get_single_user(self, user_id):
        result = user_obj.get_user(user_id)
        if result:
            return jsonify({"status":200,
            "data":result,
            "message":"You have fetched user"})
        return jsonify({"status":200,
            "error":"User doesnot exist.Retry with valid Id"})


    def add_reporter(self, *args):
        user_data = request.get_json()
        firstname = user_data.get('firstname')
        lastname = user_data.get('lastname')
        othernames = user_data.get('othernames')
        email = user_data.get('email')
        phone_number = user_data.get('phone_number')
        username = user_data.get('username')
        password = user_data.get('password')
        invalid_user = validator.validate_add_user(
            firstname, lastname, username, email, password,
            phone_number, othernames)
        if invalid_user:
            return invalid_user
        new_user = user_obj.create_user(firstname, lastname, username, password, email, phone_number)
        existent_reporter = user_obj.signup_search_user(email)
        if existent_reporter:
            return existent_reporter
        if new_user:
            return jsonify({
                "status": 201,
                "data": new_user,
                "message": "signup successful"
            })
        return jsonify({
                        "status": 400,
                        "message": "signup failed"
                    })

    def signin(self, args):
        data = request.get_json()
        username  = data.get('username')
        password = data.get('password')
        returned_user = user_obj.login_search_user(username)
        if not username:
            return jsonify({"msg" : "Provide Valid username"}),400

        if not password:
            return jsonify({"msg" : "Provide password"}),400
        
        if username==returned_user.get('username') and password==returned_user.get('password'):
            token_expiry = datetime.timedelta(days=1)
            user_id=returned_user.get('user_id')

            my_identity = user_id

            return jsonify({
                'token': create_access_token(
                    identity=my_identity,
                    expires_delta=token_expiry),
                'message': 'You have successfully logged in',
                'isadmin': returned_user['isadmin'],
                'status': 200})
                    

        return jsonify({
            'error': "invalid credentials. \
            Use a registered email and password",
            'status': 400})

    def fetch_users(self):
        result=user_obj.get_users()
        if result:
            return jsonify({
                "status": 200,
                "data": result,
                "message": "You are viewing registered reporters"})
        

    def fetch_user(self, userid):
        user = user_obj.get_user(userid)
        if user:
            return jsonify({
                "status": 200,
                "data": user,
                "message": "User details displayed"
            })
        return jsonify({
            "status": 404,
            "error": "user_id out of range, try again with a valid id"
        })