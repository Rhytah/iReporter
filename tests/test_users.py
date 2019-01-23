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
            othernames="funny",
            email="johnny@gmail.com",
            phone_number=8924556,
            username="jk",
            password="pass1236"

        )
        response = self.test_client.post('/api/v2/auth/signup/',
                                         data=json.dumps(new_user),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        print(response_out)
        self.assertEqual(response_out['status'], 201)
        self.assertIsInstance(response_out, dict)
        self.assertIn('signup successful', str(response_out['message']))

    def test_add_user_without_firstname(self):

        response = self.test_client.post('/api/v2/auth/signup/',
                                         data=json.dumps(self.testuser1),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('firstname is missing', str(response_out['error']))

    def test_add_user_without_lastname(self):
        response = self.test_client.post('/api/v2/auth/signup/',
                                         data=json.dumps(self.testuser2),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('lastname is missing', str(response_out['error']))

    def test_add_user_without_othernames(self):
        response = self.test_client.post('/api/v2/auth/signup/',
                                         data=json.dumps(self.testuser3),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('othernames is missing', str(response_out['error']))

    def test_add_user_with_invalid_email(self):
        response = self.test_client.post('/api/v2/auth/signup/',
                                         data=json.dumps(self.testuser4),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("Use valid email address format.\
                             ...janedoe@int.com", str(
            response_out['error']))

    def test_add_user_that_already_exists(self):

        response2 = self.test_client.post('/api/v2/auth/signup/',
                                         data=json.dumps(self.admin_user),
                                         content_type='application/json')
        response_out = json.loads(response2.data.decode())
        self.assertEqual(response_out['status'], 409)
        self.assertIn("User already exists", str(response_out['error']))

    def test_user_login(self):
        credentials = dict(username="jk", password="pass1236")
        new_user = dict(
            firstname="sunny",
            lastname="tamale",
            othernames="funny",
            email="johnny@gmail.com",
            phone_number=8924556,
            username="jk",
            password="pass1236"

        )
        response = self.test_client.post('/api/v2/auth/signup/',
                                         data=json.dumps(new_user),
                                         content_type='application/json')
        response = self.test_client.post('/api/v2/auth/login/',
                                         content_type='application/json',
                                         data=json.dumps(credentials))
        response_out = json.loads(response.data.decode())
        self.assertIn("You have successfully logged in",
                      str(response_out['message']))
        self.assertEqual(response_out['status'], 200)