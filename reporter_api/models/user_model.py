users = []

class User:
    def __init__(self,user_id,firstname,lastname,othernames, email,phoneNumber,username,registered,isAdmin):
        self.user_id, = user_id
        self.firstname = firstname
        