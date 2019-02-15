import re
from flask import jsonify


class Validation:

    def validate_incident(self, lat,long, image, video, comment):
        if not lat :
            return jsonify({
                "status": 400,
                "error": "latitude is missing"})
        if not isinstance(lat,float):
            return jsonify({
                "status": 400,
                "error": "use proper format as float values, 0.368 "
            })
        if not long :
            return jsonify({
                "status": 400,
                "error": "longitude is missing"})
        if not isinstance(lat,float):
            return jsonify({
                "status": 400,
                "error": "use proper format as float values, 32.368 "
            })
        if not image :
            return jsonify({
                "status": 400,
                "error": "image is missing"})

        if not video :
            return jsonify({
                "status": 400,
                "error": "video is missing"})
        if not comment or comment.isspace():
            return jsonify({
                "status": 400,
                "error": "comment is missing"})

    def validate_location(self, lat,long):
        if not lat:
            return jsonify({
                "status": 400,
                "error": "latitude is missing"})
        if not isinstance(lat, float):
            return jsonify({
                "status": 400,
                "error": "latitute must be a float value"
            })
        if not long:
            return jsonify({
                "status": 400,
                "error": "longitude is missing"})
        if not isinstance(long, float):
            return jsonify({
                "status": 400,
                "error": "longitude must be a float value"
            })


    def validate_comment(self, comment):
        if not comment:
            return jsonify({
                "status": 400,
                "error": "comment is missing"})
        if not isinstance(comment, str):
            return jsonify({
                "status": 400,
                "error": "comment must be a string"
            })

    def validate_status(self, status):
        status_messages = [
            'under investigation',
            'rejected',
            'resolved'
        ]
        if not status:
            return jsonify({
                "status": 400,
                "error": "status is missing"})
        if not isinstance(status, str):
            return jsonify({
                "status": 400,
                "error": "status must be a string"
            })
        if status not in status_messages:
            return jsonify({
                "status": 400,
                "error": "status can only be changed to \
                either under investigation or resolved"})
