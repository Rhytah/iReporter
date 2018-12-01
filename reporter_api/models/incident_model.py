import datetime
class Incident:
    def __init__(self):
        self.incidents =[]

    def get_incidents(self):
        return self.incidents
class Redflag(Incident):
    def __init__(self):
        self.redflags=[]

    def create_redflag(self,args):
        redflag=dict(
            redflag_id= len(self.redflags)+1,
            created_on =datetime.datetime.now(),
            created_by=args['created_by'],
            incident_type = "redflag",
            location = args['location'],
            status = "draft",
            image = args['image'],
            video = args['video'],
            comment = args['comment']
        )

        self.redflags.append(redflag)

        return redflag

    def get_redflags(self):
        return self.redflags


    def get_redflag(self,redflag_id):
        for redflag in self.redflags:
            if redflag['redflag_id'] ==redflag_id:
                return redflag
    