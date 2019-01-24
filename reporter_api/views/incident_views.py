from flask import Flask, json, jsonify, request,Blueprint,current_app as app
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from reporter_api.controllers.incidents_controllers import IncidentsController

incident = Blueprint("incident",__name__)
incidents_controller = IncidentsController()


@incident.route('/api/v2/red-flags/', methods=['GET'])
@incident.route('/api/v2/red-flags', methods=['GET'])
def fetch_red_flags():
    return incidents_controller.fetch_all_redflags()


@incident.route('/api/v2/red-flags/<int:redflag_id>/', methods=['GET'])
@incident.route('/api/v2/red-flags/<int:redflag_id>', methods=['GET'])
def fetch_single_red_flag(redflag_id):
    return incidents_controller.fetch_specific_redflag(redflag_id)


@incident.route('/api/v2/red-flags/', methods=['POST'])
@incident.route('/api/v2/red-flags', methods=['POST'])
@jwt_required
def add_red_flag():
    request_data = request.get_json()
    return incidents_controller.add_redflag(request_data)


@incident.route('/api/v2/red-flags/<int:redflag_id>/', methods=['DELETE'])
@incident.route('/api/v2/red-flags/<int:redflag_id>', methods=['DELETE'])
def delete_redflag(redflag_id):
    return incidents_controller.delete_redflag(redflag_id)


@incident.route('/api/v2/red-flags/<int:redflag_id>/location/', methods=['PATCH'])
@incident.route('/api/v2/red-flags/<int:redflag_id>/location', methods=['PATCH'])
def edit_location(redflag_id):
    data = request.get_json()
    location = data.get('location')

    return incidents_controller.edit_location(location,redflag_id)


@incident.route('/api/v2/red-flags/<int:redflag_id>/comment/', methods=['PATCH'])
@incident.route('/api/v2/red-flags/<int:redflag_id>/comment', methods=['PATCH'])
def edit_comment(redflag_id):
    data = request.get_json()
    comment = data.get('comment')
    return incidents_controller.edit_comment(comment,redflag_id)


@incident.route('/api/v2/interventions/<int:redflag_id>/status/', methods=['PATCH'])
@incident.route('/api/v2/interventions/<int:redflag_id>/status', methods=['PATCH'])
@jwt_required
def edit_status(redflag_id):
    current_user = get_jwt_identity()
    isadmin = current_user.get('isadmin')
    request_data = request.get_json()
    status = request_data.get('status')
    if isadmin is True:
        return incidents_controller.edit_status(status,redflag_id)

    return jsonify({
        "status": 401,
        "message": "Only admins can change status of a red-flag"
        })

# intervention routes
@incident.route('/api/v2/interventions/', methods=['POST'])
@incident.route('/api/v2/interventions', methods=['POST'])
@jwt_required
def add_intervention():
    request_data = request.get_json()
    return incidents_controller.add_intervention(request_data)

@incident.route('/api/v2/interventions/', methods=['GET'])
@incident.route('/api/v2/interventions', methods=['GET'])
def fetch_interventions():
    return incidents_controller.fetch_interventions()

@incident.route('/api/v2/interventions/<int:intervention_id>/', methods=['GET'])
@incident.route('/api/v2/interventions/<int:intervention_id>', methods=['GET'])
def fetch_intervention(intervention_id):
    return incidents_controller.fetch_specific_intervention(intervention_id)

@incident.route('/api/v2/interventions/<int:intervention_id>/', methods=['DELETE'])
@incident.route('/api/v2/interventions/<int:intervention_id>', methods=['DELETE'])
def delete_intervention(intervention_id):
    return incidents_controller.delete_specific_intervention(intervention_id)

@incident.route('/api/v2/interventions/<int:intervention_id>/location/', methods=['PATCH'])
@incident.route('/api/v2/interventions/<int:intervention_id>/location', methods=['PATCH'])
def edit_interventionlocation(intervention_id):


    return incidents_controller.edit_interventionlocation(intervention_id)


@incident.route('/api/v2/interventions/<int:intervention_id>/comment/', methods=['PATCH'])
@incident.route('/api/v2/interventions/<int:intervention_id>/comment', methods=['PATCH'])
def edit_interventioncomment(intervention_id):
 
    return incidents_controller.edit_interventioncomment(intervention_id)