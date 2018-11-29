
incidents = []
class Incident:
    def __init__(self):
        self.incidents =incidents

    def create_incident(self,args):
        incident=dict(
            _id= len(self.incidents)+1,
            createdOn =args['createdOn'],
            createdBy=args['createdBy'],
            type = args['type'],
            location = args['location'],
            status = args['status'],
            image = args['image'],
            video = args['video'],
            comment = args['comment']
        )

        self.incidents.append(incident)

        return incident

    def get_incidents(self):
        return self.incidents

    def get_incident(self,_id):
        for incident in self.incidents:
            if incident['_id'] ==_id:
                return incident
    