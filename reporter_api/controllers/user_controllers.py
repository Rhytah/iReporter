from reporter_api.models.user_model import Reporter
from flask import jsonify,json,request
from reporter_api import app
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity
from reporter_api.utilities.user_validators import UserValidator
import datetime

reporter_obj = Reporter()
validator = UserValidator()

class User_controller:
    def __init__(self):
        self.reporters = reporter_obj.get_users()
    
    def add_reporter(self,*args):
        user_data = request.get_json()
        user_id = len(self.reporters)+1
        isadmin = "Not Admin"
        registered = datetime.datetime.now()
        firstname = user_data.get('firstname')
        lastname = user_data.get('lastname')
        othernames = user_data.get('othernames')
        email = user_data.get('email')
        phone_number = user_data.get('phone_number')
        username = user_data.get('username')
        password = user_data.get('password')
        invalid_user=validator.validate_add_user(firstname,lastname,username,email,password,phone_number,othernames)
        if invalid_user:
            return invalid_user
        new_reporter = {'user_id':user_id,'registered':registered,'firstname':firstname,'lastname':lastname,'othernames':othernames,'email':email,'phone_number':phone_number,'username':username,"isadmin":isadmin,'password':password}
        reporter =reporter_obj.search_reporter(username,password)
        if reporter:
                return jsonify({
                    "status":400,
                    "error":"user already exits"
                })
        reporter_obj.create_reporter(user_data)

        return jsonify ({
            "status":201,
            "data":new_reporter,
            "message":"signup successful"
        })
    def signin(self,args):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        access_token = create_access_token(identity=username)
        reporter=reporter_obj.search_reporter(username,password)
    
        if not reporter:
            return jsonify({
                "status":400,
                "error":"invalid credentials. Use a registered username and password"})
        return jsonify({
            "status":200,
            "message":f"{username} ,you have successfully logged in",
            "data": f"This is your token {access_token}"})  


    def fetch_reporters(self):
        if len(self.reporters)<1:
            return jsonify({
                "status":200,
                "message": "No reporters registered"
            })
        return jsonify({
            "status":200,
            "data":self.reporters,
            "message":"You are viewing registered reporters"
        })
    
    def fetch_reporter(self,user_id):
        reporter=reporter_obj.get_reporter(user_id)
        if reporter:
            return jsonify({
                "status":200,
                "data":reporter,
                "message":"Reporter details displayed"
            })
        return jsonify({
            "status":400,
            "error":"user_id out of range, try again with a valid id"
        })
