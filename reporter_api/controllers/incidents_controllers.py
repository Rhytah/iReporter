from reporter_api.models.incident_model import Redflag, Intervention
from flask import jsonify, request, current_app as app
from reporter_api.utilities.incident_validators import Validation
from flask_jwt_extended import get_jwt_identity
from database.server import DatabaseConnect

import datetime
import json
db = DatabaseConnect()
validator = Validation()

redflag_obj = Redflag()
intervention_obj = Intervention()


class IncidentsController:

    def add_redflag(self, *args):
        current_user = get_jwt_identity()
        userid = current_user['userid']
        data = request.get_json()
        status = "draft"
        created_by = userid
        created_on = datetime.datetime.now()
        location = data.get('location')
        image = data.get('image')
        video = data.get('video')
        comment = data.get('comment')
        invalid_redflag = validator.validate_incident(
            location, image, video, comment)
        if invalid_redflag:
            return invalid_redflag

        new_redflag = redflag_obj.create_redflag(
            created_by, created_on, status, location, image, video, comment)

        return jsonify({
            "data": new_redflag,
            "message": "Successfully added red-flag"
        }),201

    def fetch_all_redflags(self):
        result = redflag_obj.get_redflags()
        if result:
            return jsonify({

                "data": result,
                "message": "These are the recorded red-flags"
            })
        return jsonify({
            "error": "These are no found red-flags"
        }), 404

    def fetch_specific_redflag(self, redflag_id):
        redflag = redflag_obj.get_redflag(redflag_id)
        if not redflag:
            return jsonify({
                "message": "Redflag not found."
            }), 404
        return jsonify({
            "data": redflag,
            "message": "red-flag details displayed"
        })

    def delete_redflag(self, redflag_id):
        redflag = redflag_obj.get_redflag(redflag_id)
        response = redflag_obj.delete_redflag(redflag_id)
        if response:
            return jsonify({
                "data": redflag,
                "message": "This displayed red-flag has been deleted"
            })
        return jsonify({
            "message": "Redflag not found."
        }),404

    def edit_location(self, location, redflag_id):
        request_data = request.data
        data = json.loads(request_data)
        location = data['location']
        invalid_location = validator.validate_location(location)
        location = redflag_obj.modify_location(location, redflag_id)

        if invalid_location:
            return invalid_location
        if location:
            return jsonify({
                "message": f"You have changed red flag's location to{location}"
            }), 200
        return jsonify({
            "message": "Redflag not found."}),404

    def edit_comment(self, comment, redflag_id):
        data = request.get_json()
        comment = data.get('comment')

        invalid_comment = validator.validate_comment(comment)
        if invalid_comment:
            return invalid_comment
        comment = redflag_obj.modify_comment(comment, redflag_id)

        if comment:
            return jsonify({
                "message": f"You have changed red flag's comment to{comment}"
            }), 200
        return jsonify({
            "message": "Redflag not found."}),404

    def edit_status(self, redflag_id):
        status_data = request.get_json()
        status = status_data['status']
        invalid_status = validator.validate_status(status)
        if invalid_status:
            return invalid_status
        status = redflag_obj.modify_status(status, redflag_id)
        if status:
            return jsonify({
                "message": f"You have changed red flag's status to{status}"
            }), 200
        return jsonify({
            "message": "Redflag not found."}),404

    # interventions controllers
    def add_intervention(self, *args):
        current_user = get_jwt_identity()
        userid = current_user['userid']
        data = request.get_json()
        status = "draft"
        created_by = userid
        created_on = datetime.datetime.now()
        status = "draft"
        location = data.get('location')
        image = data.get('image')
        video = data.get('video')
        comment = data.get('comment')
        invalid_intervention = validator.validate_incident(
            location, image, video, comment)
        if invalid_intervention:
            return invalid_intervention
        new_intervention = intervention_obj.create_intervention(
            created_by, created_on, status, location, image, video, comment)

        return jsonify({
            "data": new_intervention,
            "message": "Successfully added intervention"
        }),201

    def fetch_interventions(self):
        result = intervention_obj.get_interventions()
        if result:
            return jsonify({
                "data": result,
                "message": "These are the Intervention records"
            })
        return jsonify({
            "error": "Interventions not found"
        }),404

    def fetch_specific_intervention(self, intervention_id):
        result = intervention_obj.get_intervention(intervention_id)
        if result:
            return jsonify({
                "data": result,
                "message": "Successfully fetched intervention record"
            })
        return jsonify({
            "error": "Intervention record not found."
        }),404

    def delete_specific_intervention(self, intervention_id):
        result = intervention_obj.get_intervention(intervention_id)
        response = intervention_obj.delete_intervention(intervention_id)
        if response:
            return jsonify({
                "data": result,
                "message": "This intervention has been deleted"
            })
        return jsonify({
            "error": "Intervention record not found."
        }),404

    def edit_interventionlocation(self, intervention_id):
        data = request.get_json()
        location = data.get('location')

        invalid_location = validator.validate_location(location)

        if invalid_location:
            return invalid_location
        location = intervention_obj.modify_interventionlocation(
            location, intervention_id)

        if location:
            return jsonify({
                "data": intervention_id,
                "message": "You have changed intervention's location"
            })
        return jsonify({
            "error": "Intervention record not found."}),404

    def edit_interventioncomment(self, intervention_id):

        data = request.get_json()
        comment = data.get('comment')

        invalid_comment = validator.validate_comment(comment)
        if invalid_comment:
            return invalid_comment
        comment = intervention_obj.modify_interventioncomment(
            comment, intervention_id)
        if comment:
            return jsonify({
                "data": intervention_id,
                "message": "You have changed intervention's comment"
            }), 200
        return jsonify({
            "error": "Intervention record not found."}),404
