from flask import Flask, jsonify,request,json
from reporter_api import app
from reporter_api.controllers.incidents_controllers import IncidentsController
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity



incidents_controller=IncidentsController()
@app.route('/api/v1/red-flags',methods=['GET'])
def fetch_red_flags():
    return incidents_controller.fetch_all_redflags()

@app.route('/api/v1/red-flags/<int:_id>', methods = ['GET'])
def fetch_single_red_flag(_id):
    return incidents_controller.fetch_specific_redflag(_id)

@app.route('/api/v1/red-flags',methods=['POST'])
@jwt_required
def add_red_flag():
    request_data=request.get_json()
    return incidents_controller.add_redflag(request_data)

@app.route('/api/v1/red-flags/<int:_id>',methods=['DELETE'])
def delete_redflag(_id):
    return incidents_controller.delete_redflag(_id)

@app.route('/api/v1/red-flags/<int:_id>/location', methods =['PATCH'])
def edit_location(_id):
    return incidents_controller.edit_location(_id)

@app.route('/api/v1/red-flags/<int:_id>/comment', methods =['PATCH'])
def edit_comment(_id):
    return incidents_controller.edit_comment(_id)