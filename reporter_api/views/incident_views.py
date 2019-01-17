from flask import Flask, jsonify,request,json
from reporter_api import app
from reporter_api.controllers.incidents_controllers import IncidentsController
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity



incidents_controller=IncidentsController()
@app.route('/api/v1/red-flags/',methods=['GET'])
def fetch_red_flags():
    return incidents_controller.fetch_all_redflags()

@app.route('/api/v1/red-flags/<int:redflag_id>/', methods = ['GET'])
def fetch_single_red_flag(redflag_id):
    return incidents_controller.fetch_specific_redflag(redflag_id)

@app.route('/api/v1/red-flags/',methods=['POST'])
@jwt_required
def add_red_flag():
    request_data=request.get_json()
    return incidents_controller.add_redflag(request_data)

@app.route('/api/v1/red-flags/<int:redflag_id>/',methods=['DELETE'])
def delete_redflag(redflag_id):
    return incidents_controller.delete_redflag(redflag_id)

@app.route('/api/v1/red-flags/<int:redflag_id>/location/', methods =['PATCH'])
def edit_location(redflag_id):
    return incidents_controller.edit_location(redflag_id)

@app.route('/api/v1/red-flags/<int:redflag_id>/comment/', methods =['PATCH'])
def edit_comment(redflag_id):
    return incidents_controller.edit_comment(redflag_id)

@app.route('/api/v1/red-flags/<int:redflag_id>/status/', methods =['PATCH'])
@jwt_required
def edit_status(redflag_id):
    current_user = get_jwt_identity()
    isadmin = current_user.get("isadmin")
    if isadmin == True:
        return incidents_controller.edit_status(redflag_id)
    
    return jsonify({
        "status":401,
        "message": "Only admins can change status of a red-flag"
        }) 