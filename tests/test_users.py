from reporter_api import app
from tests.test_base import BaseTestCase
from reporter_api.views import user_views
import json
import re

class UserTestase(BaseTestCase):

    def test_add_user(self):
        response= self.test_client.post('/api/v1/auth/signup',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],201)
        self.assertIsInstance(response_out,dict)
        self.assertIn("signup successful",str(response_out['message']))
        
    def test_add_user_without_firstname(self):

        response= self.test_client.post('/api/v1/auth/signup',
        data=json.dumps(self.testuser1),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn('firstname is missing',str(response_out['error']))

    def test_add_user_without_lastname(self):
        response= self.test_client.post('/api/v1/auth/signup',
        data=json.dumps(self.testuser2),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn('lastname is missing',str(response_out['error']))

    def test_add_user_without_othernames(self):
        response= self.test_client.post('/api/v1/auth/signup',
        data=json.dumps(self.testuser3),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn('othernames is missing',str(response_out['error']))

    def test_add_user_with_invalid_email(self):
        response= self.test_client.post('/api/v1/auth/signup',
        data=json.dumps(self.testuser4),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn("Use valid email address format. ...janedoe@int.com",str(response_out['error']))

    def test_add_user_that_already_exists(self):
        response= self.test_client.post('/api/v1/auth/signup',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],400)
        self.assertIn("user already exits",str(response_out['error']))

    def test_user_login(self):
        credentials = dict(username="sunnyk",password="pass1236")
        response= self.test_client.post('/api/v1/auth/login',
        content_type='application/json',
        data=json.dumps(credentials))
        response_out=json.loads(response.data.decode())
        self.assertIn("sunnyk ,you have successfully logged in", str(response_out['message']))
        self.assertEqual(response_out['status'],200)

    def test_fetch_reporters(self):
        response=self.test_client.get('/api/v1/auth/users')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],200)
        self.assertIn("You are viewing registered reporters",str(response_out['message']))
    
    def test_fetch_specific_reporter(self):
        response=self.test_client.get('/api/v1/auth/users/1',
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],200)
        self.assertIn("Reporter details displayed",str(response_out['message']))

    def test_add_user_with_symbols(self):
        testuser6= dict(
            firstname="##33 3r",
            lastname="tamale",
            othernames = "funny",
            phone_number =25678924556,
            username="username",
            password= "pass1236"
        )       
