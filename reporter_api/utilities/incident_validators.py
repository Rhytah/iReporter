import re

class Validation:

    
    def validate_incident(self,location,image,video,comment, createdBy):
        if not location or location == " ":
            return "location is missing"
        if not image or image == " ":
            return "image is missing"
        if not video or video == " ":
            return "video is missing"
        if not comment:
            return "comment is missing"
        # if not re.match(r'"^([a-zA-Z\d]+[-_])*[a-zA-Z\d*]+$"', comment):
        #     return "comment must have no white spaces"
        if not createdBy or createdBy=="":
            return "createdBy is missing"

    def validate_location(self,location):
        if not location or location == " ":
            return "location is missing"

    def validate_comment(self,comment):
        if not comment:
            return "comment is missing"
