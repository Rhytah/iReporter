import re
from flask import jsonify
class Validation:

    def validate_incident(self,location,image,video,comment):
        if not location:
            return jsonify({
                "status":400,
                "message":"location is missing"})
        if not re.match(r"(^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$)", location):
            return({
                "status":400,
                "message":"use proper format"
            })
        
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
        return isinstance(comment,str)
