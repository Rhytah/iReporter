from flask import Flask,jsonify,json, request
from reporter_api import app
from reporter_api.controllers.user_controllers import User_controller
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity

user_controller = User_controller()

@app.route('/api/v1/auth/signup', methods =['POST'])
def signup():
    request_data = request.get_json()
    return user_controller.add_reporter(request_data)

@app.route('/api/v1/auth/users', methods = ['GET'])
def fetch_users():
    return user_controller.fetch_reporters()

@app.route('/api/v1/auth/login', methods =['POST'])
def login():
    user_data=request.get_json()
    return user_controller.signin(user_data)  

@app.route('/api/v1/auth/users/<int:user_id>',methods = ['GET'])
def get_a_reporter(user_id):
    return user_controller.fetch_reporter(user_id)