import re
from flask import jsonify
class Validation:

    def validate_incident(self,location,image,video,comment):
        if not location:
            return jsonify({
                "status":400,
                "error":"location is missing"})
        if not isinstance(location,list) or len(location)!=2:
            return({
                "status":400,
                "error":"use proper format,  ["",""]"
            })
        
        if not image or image.isspace():
            return jsonify({
                "status":400,
                "error":"image is missing"})
            
        if not video or video.isspace():
            return jsonify({
                "status":400,
                "error":"video is missing"})
        if not comment or comment.isspace():
            return jsonify({
                "status":400,
                "error":"comment is missing"})

        

    def validate_location(self,location):
        if not location:
            return jsonify({
                "status":400,
                "error":"location is missing"})
        if not isinstance(location,list) or len(location)!=2:
            return({
                "status":400,
                "error":"use proper format,  ["",""]"
            })
        
    

    def validate_comment(self,comment):
        if not comment or comment.isspace():
            return jsonify({
                "status":400,
                "error":"comment is missing"})
        if not isinstance(comment,str):
            return jsonify({
                "status":400,
                "error":"comment must be a string"
            })
