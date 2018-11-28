from reporter_api.models.incident_model import Incident
from flask import jsonify, request

class IncidentsController:
    def __init__(self):
        self.incidents = []

    def add_redflag(self,args):
        incident_model = Incident()

        redflag = incident_model.create_incident(args)
        if not redflag:
            return jsonify({
                "message":"No redflags found"
            }),200
        return jsonify ({
            "status":201,
            "red-flag":redflag
        }),201

        

