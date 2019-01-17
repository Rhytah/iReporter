redflags = []
class Redflag:
    
    def __init__(self,redflag_id,created_on,created_by,incident_type,status,location,image,video,comment):
        self.redflag_id = redflag_id
        self.created_on = created_on
        self.created_by = created_by
        self.incident_type = incident_type
        self.status= status
        self.location = location
        self.image = image
        self.video  = video
        self.comment = comment