import re
from flask import jsonify
class Validation:

    
    def validate_incident(self,location,image,video,comment, created_by):
        if not location or location.isspace():
            return jsonify({
                "status":400,
                "message":"location is missing"})
        if not image or image.isspace():
            return jsonify({
                "status":400,
                "message":"image is missing"})
            
        if not video or video.isspace():
            return jsonify({
                "status":400,
                "message":"video is missing"})
        if not comment or comment.isspace():
            return jsonify({
                "status":400,
                "message":"comment is missing"})

        if not created_by or created_by=="":
            return jsonify({
                "status":400,
                "message":"created_by is missing"})
        

    def validate_location(self,location):
        if not location or location.isspace():
            return jsonify({
                "status":400,
                "message":"location is missing"})

    def validate_comment(self,comment):
        if not comment or comment.isspace():
            return jsonify({
                "status":400,
                "message":"comment is missing"})