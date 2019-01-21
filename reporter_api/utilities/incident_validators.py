import re
from flask import jsonify


class Validation:

    def validate_incident(self, location, image, video, comment):
        if not location:
            return jsonify({
                "status": 400,
                "error": "location is missing"})
        if not isinstance(
                location,
                list) or not len(location) == 2 or not isinstance(
                location[0],
                float) or not isinstance(
                location[1],
                float):
            return jsonify({
                "status": 400,
                "error": "use proper format as float values,  [,] "
            })

        if not image or image.isspace():
            return jsonify({
                "status": 400,
                "error": "image is missing"})

        if not video or video.isspace():
            return jsonify({
                "status": 400,
                "error": "video is missing"})
        if not comment or comment.isspace():
            return jsonify({
                "status": 400,
                "error": "comment is missing"})

    def validate_location(self, location):
        if not location:
            return jsonify({
                "status": 400,
                "error": "location is missing"})
        if not isinstance(
                location,
                list) or not len(location) == 2 or not isinstance(
                location[0],
                float) or not isinstance(
                location[1],
                float):
            return jsonify({
                "status": 400,
                "error": "use proper format as float values,  [,] "
            })

    def validate_comment(self, comment):
        if not comment or comment.isspace():
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
        if not status or status.isspace():
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
