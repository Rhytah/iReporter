import unittest
from reporter_api import app
import json

class BaseTestCase(unittest.TestCase):
   
    def setUp(self):
        self.app = app
        self.test_client = app.test_client()
        self.incident=dict(
            location = [123.01,110.36],
            image = "image",
            video = "image",
            comment = "Policeman asked for something something"
            ) 
        self.user = dict(
            firstname="sunny",
            lastname="tamale",
            othernames = "funny",
            email = "johndoe@gmail.com",
            phone_number =25678924556,
            username="sunnyk",
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
        self.reporter = dict(username='sunnyk',password='pass1236')
        self.admin_user = dict(username='admin',password='sup3rpswd')
    def post_redflag(self):
        self.test_client.post('/api/v1/auth/signup/',
                data=json.dumps(self.user),
                content_type='application/json')

        response= self.test_client.post('/api/v1/auth/login/',
                data=json.dumps(self.user),
                content_type='application/json')
        response_out=json.loads(response.data.decode())
        token = response_out['token']
        headers = {'Authorization':f'Bearer {token}'}
        response2= self.test_client.post(
            '/api/v1/red-flags/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
            )
        response_out=json.loads(response2.data.decode())

        