import re
from flask import jsonify


class Validation:

    def validate_incident(self, location, image, video, comment):
        if not location:
            return jsonify({
                "error": "location is missing"}), 422

        if not image:
            return jsonify({
                "error": "image is missing"}), 422

        if not video:
            return jsonify({

                "error": "video is missing"}), 422
        if not comment or comment.isspace():
            return jsonify({
                "error": "comment is missing"}), 422

    def validate_location(self, location):
        if not location:
            return jsonify({
                "error": "location is missing"}), 422
        if not isinstance(location, float):
            return jsonify({
                "error": "location must be a float value"
            }), 422

    def validate_comment(self, comment):
        if not comment:
            return jsonify({
                "error": "comment is missing"}), 422
        if not isinstance(comment, str):
            return jsonify({
                "error": "comment must be a string"
            }), 422

    def validate_status(self, status):
        status_messages = [
            'under investigation',
            'rejected',
            'resolved'
        ]
        if not status:
            return jsonify({
                "error": "status is missing"}), 422
        if not isinstance(status, str):
            return jsonify({
                "error": "status must be a string"
            }), 422
        if status not in status_messages:
            return jsonify({
                "error": "status can only be changed to \
                either under investigation or resolved"}), 422
