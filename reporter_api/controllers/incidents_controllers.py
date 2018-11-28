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


