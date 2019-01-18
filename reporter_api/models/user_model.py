import datetime
users = []


class Reporter:
    def __init__(self, user_id, registered, firstname, lastname, othernames, email, phone_number, username, password, isadmin):

        self.user_id = len(users)+1
        self.registered = datetime.datetime.now()
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.isadmin = False


admin = {'user_id': 1, 'firstname': "rita", 'lastname': "namono", 'othernames': "none", 'email': "hdh@mail.com",
         'phone_number': "254865268", 'username': "admin", 'password': "sup3rpswd", "isadmin": True}
