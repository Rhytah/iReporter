from reporter_api import app
from tests.test_base import BaseTestCase
from reporter_api.views import user_views
import json
import re

class UserTestcase(BaseTestCase):

    def test_add_user(self):
        new_user = dict(
            firstname="sunny",
            lastname="tamale",
            othernames = "funny",
            email = "johnny@gmail.com",
            phone_number =25678924556,
            username="jk",
            password= "pass1236"

        )    
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(new_user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        print (response_out)
        self.assertEqual(response_out['status'],201)
        self.assertIsInstance(response_out,dict)
        self.assertIn("signup successful",str(response_out['message']))
        
    def test_add_user_without_firstname(self):

        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.testuser1),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn('firstname is missing',str(response_out['error']))

    def test_add_user_without_lastname(self):
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.testuser2),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn('lastname is missing',str(response_out['error']))

    def test_add_user_without_othernames(self):
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.testuser3),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn('othernames is missing',str(response_out['error']))

    def test_add_user_with_invalid_email(self):
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.testuser4),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn("Use valid email address format. ...janedoe@int.com",str(response_out['error']))

    def test_add_user_that_already_exists(self):
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],409)
        self.assertIn("user already exits",str(response_out['error']))

    def test_invalid_user_login(self):
        credentials = dict(username="Kengrow",password="pass1236")
        response= self.test_client.post('/api/v1/auth/login/',
        content_type='application/json',
        data=json.dumps(credentials))
        response_out=json.loads(response.data.decode())
        self.assertIn("invalid credentials. Use a registered username and password", str(response_out['error']))
        self.assertEqual(response_out['status'],400)

    def test_user_login(self):
        credentials = dict(username="sunnyk",password="pass1236")
        response= self.test_client.post('/api/v1/auth/login/',
        content_type='application/json',
        data=json.dumps(credentials))
        response_out=json.loads(response.data.decode())
        self.assertIn("sunnyk ,you have successfully logged in", str(response_out['message']))
        self.assertEqual(response_out['status'],200)

 
 
    def test_fetch_reporters(self):
        with self.app.app_context():
            response= self.test_client.post('/api/v1/auth/login/',
                data=json.dumps(self.admin_user),
                content_type='application/json')
            response_out=json.loads(response.data.decode())
            token = response_out['token']
            headers = {'Authorization':f'Bearer {token}'}

            response2=self.test_client.get(
                '/api/v1/auth/users/',
                content_type='application/json',
                headers = headers)
            response_out=json.loads(response2.data.decode())
        self.assertEqual(response_out['status'],200)
        self.assertIn("You are viewing registered reporters",str(response_out['message']))
        self.assertNotIn("No reporters registered",str(response_out['message']))

    def test_fetch_reporters_as_nonadmin(self):
        with self.app.app_context():
            response= self.test_client.post('/api/v1/auth/login/',
                data=json.dumps(self.reporter),
                content_type='application/json')
            response_out=json.loads(response.data.decode())
            token = response_out['token']
            headers = {'Authorization':f'Bearer {token}'}

            response2=self.test_client.get(
                '/api/v1/auth/users/',
                content_type='application/json',
                headers = headers)
            response_out=json.loads(response2.data.decode())
        self.assertEqual(response_out['status'],401)
        self.assertIn('Only admins can see users',str(response_out['error']))
       
    
    def test_fetch_specific_reporter(self):
        response=self.test_client.get('/api/v1/auth/users/1/',
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],200)
        self.assertIn("Reporter details displayed",str(response_out['message']))

    def test_fetch_specific_reporter_out_of_range(self):
        response=self.test_client.get('/api/v1/auth/users/20/',
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],400)
        self.assertIn("user_id out of range, try again with a valid id",str(response_out['error']))

    def test_add_user_firstname_with_symbols(self):
        self.user['firstname'] = "###$%%^&"
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],400)
        self.assertIsInstance(response_out,dict)
        self.assertIn("firstname cannot be integers, have white spaces or symbols",str(response_out['error']))

    def test_add_user_lastname_with_symbols(self):
        self.user['lastname'] = "###_  @"
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],400)
        self.assertIsInstance(response_out,dict)
        self.assertIn("lastname cannot be integers, have white spaces or symbols",str(response_out['error']))

    def test_add_user_othernames_invalid(self):
        self.user['othernames'] = "  l@st#yujn"
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],400)
        self.assertIsInstance(response_out,dict)
        self.assertIn("othernames cannot be integers, have white spaces or symbols",str(response_out['error']))

    def test_add_user_invalid_password(self):
        self.user['password'] = "pass"
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],400)
        self.assertIsInstance(response_out,dict)
        self.assertIn("['Password should be at least 6 characters longuppercase letters: A-Z', 'lowercase letters- a-z', 'numbers: 0-9', 'any of the special characters: @#$%^&+=']",str(response_out['error']))
    
    def test_add_user_username_invalid(self):
        self.user['username'] = "  l@st#yujn"
        response= self.test_client.post('/api/v1/auth/signup/',
        data=json.dumps(self.user),
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],400)
        self.assertIsInstance(response_out,dict)
        self.assertIn("username cannot be integers,have white spaces or symbols",str(response_out['error']))