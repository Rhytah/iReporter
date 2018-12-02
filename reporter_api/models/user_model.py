import datetime

class User:
    def __init__(self):

        self.users = []

    def get_users(self):
        return self.users
class Reporter(User):
    def __init__(self):
        super().__init__()

    def create_reporter(self,args):
        reporter=dict(
            user_id= len(self.users)+1,
            registered =datetime.datetime.now(),
            firstname=args['firstname'],
            lastname = args['lastname'],
            othernames =args['othernames'],
            email = args['email'],
            phone_number = args['phone_number'],
            username = args['username'],
            isadmin= "Not Admin"
                    )
        self.users.append(reporter)

        return reporter

    def get_reporter(self,reporter_id):
        for reporter in self.users:
            if reporter['reporter_id'] ==reporter_id:
                return reporter