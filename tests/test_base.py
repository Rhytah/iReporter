import unittest
from reporter_api import app
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity


class BaseTestCase(unittest.TestCase):
   
    def setUp(self):
        self.app = app
        self.test_client = app.test_client()
        self.incident=dict(
            location = '123.01.56.78',
            image = "image",
            video = "image",
            comment = "Policeman asked for something something"
            )
    
        self.token = create_access_token
        self.header = {'Authorization':f'Bearer {self.token}'}  
        self.user = dict(
            firstname="sunny",
            lastname="tamale",
            othernames = "funny",
            email = "johndoe@gmail.com",
            phone_number =25678924556,
            username="username",
            password= "pass1236"

        )          
        self.testuser1 = dict(
            lastname="tamale",
            othernames = "funny",
            email = "johndoe@gmail.com",
            phone_number =25678924556,
            username="username",
            password= "pass1236"

        ) 
        self.testuser2 = dict(
            firstname="sunny",
            othernames = "funny",
            email = "johndoe@gmail.com",
            phone_number =25678924556,
            username="username",
            password= "pass1236"

        ) 
        self.testuser3 = dict(
            firstname="sunny",
            lastname="tamale",
            email = "johndoe@gmail.com",
            phone_number =25678924556,
            username="username",
            password= "pass1236"
        )       

        self.testuser4 = dict(
            firstname="sunny",
            lastname="tamale",
            othernames = "funny",
            email="someemail",
            phone_number =25678924556,
            username="username",
            password= "pass1236"
        )       
        
        self.testuser5 = dict(
            firstname="sunny",
            lastname="tamale",
            othernames = "funny",
            phone_number =25678924556,
            username="username",
            password= "pass1236"
        )       
