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
        redflag=incident_model.get_incident(_id)
        if not redflag:
            return jsonify({
                "status":400,
                "message":"Out of range red-flag id,Try again with a valid id"
            }),200

        return jsonify({
            "status":200,
            "data":redflag
        }),200
    
    def delete_redflag(self,_id):
        redflag=incident_model.get_incident(_id)
        incidents= incident_model.get_incidents()
        if redflag:
            incidents.remove(redflag)
            return jsonify({
                "status":200,
                "data":f'{redflag} has been deleted'
            }),200
        return jsonify({
            "status":400,
            "message":"redflag out of range, use valid id"
        }),200

    

    def edit_location(self,_id):
        redflag=incident_model.get_incident(_id)
        data = request.get_json()                
        if redflag:
            print (redflag['location'])
            location = data.get('location')
            new_location = location
                      
            redflag['location'] = new_location
            return jsonify({
                "message":f"You have changed red flag's location to{location}"
            }),200
        return jsonify({
            "status":200,
            "message":"Invalid id, try again"})

    def edit_comment(self,_id):
        redflag=incident_model.get_incident(_id)
        data = request.get_json()                
        if redflag:
            comment = data.get('comment')
            new_comment = comment
            redflag['comment'] = new_comment
            return jsonify({
                "message":f"You have changed red flag's comment to {comment}"
            }),200
        return jsonify({
            "status":400,
            "message":"Invalid id, try again"})

