from reporter_api.models.incident_model import Redflag,Incident
from flask import jsonify, request
from reporter_api.utilities.incident_validators import Validation
import datetime
import json

redflag_obj = Redflag()
validator = Validation()

class IncidentsController:
    def __init__(self):
        self.redflags=redflag_obj.get_incidents()

    def add_redflag(self,data):
        data = request.get_json()
        redflag_id = len(self.redflags)+1
        created_on =datetime.datetime.now()
        incident_type = "redflag"
        status = "draft"
        created_by = data.get('created_by')
        location = data.get('location')
        image = data.get ('image')
        video = data.get('video')
        comment = data.get('comment')
        invalid_redflag= validator.validate_incident(location,image,video,comment,created_by)
        if invalid_redflag:
            return invalid_redflag
        new_redflag = {"redflag_id":redflag_id,"created_on":created_on,"created_by":created_by,"incident_type":incident_type,"location":location,"status":status,"image":image,"video":video,"comment":comment}
        
        redflag_obj.create_redflag(data)
        if not new_redflag:
            return jsonify({
                "message":"No redflags found"
            }),200
        return jsonify ({
            "status":201,
            "red-flag":new_redflag
        }),201

    def fetch_all_redflags(self):
        if not self.redflags or len(self.redflags) < 1 :
            return jsonify({
                "status":200,
                "message": "No red-flags found"
            }),200

        return jsonify({
            "status":200,
            "data":self.redflags
        })
    def fetch_specific_redflag(self,redflag_id):
        redflag=redflag_obj.get_redflag(redflag_id)
        if not redflag:
            return jsonify({
                "status":400,
                "message":"Out of range red-flag id,Try again with a valid id"
            }),200

        return jsonify({
            "status":200,
            "data":redflag
        }),200
    
    def delete_redflag(self,redflag_id):
        redflag=redflag_obj.get_redflag(redflag_id)
        if redflag:
            self.redflags.remove(redflag)
            return jsonify({
                "status":200,
                "data":f'{redflag} has been deleted'
            }),200
        return jsonify({
            "status":400,
            "message":"redflag out of range, use valid id"
        }),200

    

    def edit_location(self,redflag_id):
        redflag=redflag_obj.get_redflag(redflag_id)
        data = request.get_json()                
        if redflag:
            print (redflag['location'])
            location = data.get('location')
            invalid_location =validator.validate_location(location)
            if invalid_location:
                return invalid_location
            new_location = location
            redflag['location'] = new_location
            return jsonify({
                "message":f"You have changed red flag's location to{location}"
            }),200
        return jsonify({
            "status":200,
            "message":"Invalid id, try again"})

    def edit_comment(self,redflag_id):
        redflag=redflag_obj.get_redflag(redflag_id)
        data = request.get_json()                
        if redflag:
            comment = data.get('comment')
            invalid_comment =validator.validate_comment(comment)
            if invalid_comment:
                return invalid_comment
            new_comment = comment
            redflag['comment'] = new_comment
            return jsonify({
                "message":f"You have changed red flag's comment to {comment}"
            }),200
        return jsonify({
            "status":400,
            "message":"Invalid id, try again"})