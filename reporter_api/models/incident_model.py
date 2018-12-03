import datetime
from flask_jwt_extended import JWTManager,get_jwt_identity

class Incident:
    def __init__(self):
        self.incidents =[]

    def get_incidents(self):
        return self.incidents
class Redflag(Incident):
    def __init__(self):
        super().__init__()

    def create_redflag(self,args):
        redflag=dict(
            redflag_id= len(self.incidents)+1,
            created_on =datetime.datetime.now(),
            created_by=get_jwt_identity(),
            incident_type = "redflag",
            location = args['location'],
            status = "draft",
            image = args['image'],
            video = args['video'],
            comment = args['comment']
        )
        self.incidents.append(redflag)
        return redflag

    def get_redflag(self,redflag_id):
        for redflag in self.incidents:
            if redflag['redflag_id'] ==redflag_id:
                return redflag