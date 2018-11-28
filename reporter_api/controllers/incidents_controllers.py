from reporter_api.models.incident_model import Incident
from flask import jsonify, request

incident_model = Incident()
class IncidentsController:
    def __init__(self):
        self.incidents = []

    def add_redflag(self,args):
        redflag = incident_model.create_incident(args)
        if not redflag:
            return jsonify({
                "message":"No redflags found"
            }),200
        return jsonify ({
            "status":201,
            "red-flag":redflag
        }),201

    def fetch_all_redflags(self):
        incidents= incident_model.get_incidents()
        if not incidents or len(incidents) < 1 :
            return jsonify({
                "status":200,
                "message": "No red-flags found"
            }),200

        return jsonify({
            "status":200,
            "data":incidents
        })
    def fetch_specific_redflag(self,_id):
        redflag=incident_model.get_an_incident(_id)
        if not redflag:
            return jsonify({
                "status":200,
                "message":"Out of range red-flag id,Try again with a valid id"
            }),200

        return jsonify({
            "status":200,
            "data":redflag
        }),200


