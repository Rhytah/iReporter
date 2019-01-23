from reporter_api import app
from tests.test_base import BaseTestCase
from reporter_api.views import incident_views
import json

from flask_jwt_extended import JWTManager, create_access_token


class RedflagTestCase(BaseTestCase):
    
    def test_add_redflag_with_token(self):

        self.test_client.post('/api/v2/auth/signup/',
                              data=json.dumps(self.user),
                              content_type='application/json')

        response = self.test_client.post('/api/v2/auth/login/',
                                         data=json.dumps(self.user),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        token = response_out['token']
        headers = {'Authorization': f'Bearer {token}'}

        response2 = self.test_client.post(
            '/api/v2/red-flags/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )
        response_out = json.loads(response2.data.decode())
        print(response_out)
        self.assertEqual(response_out['status'], 201)
        self.assertIsInstance(response_out, dict)
        self.assertIn("Successfully added red-flag",
                      str(response_out['message']))

    def test_fetch_all_redflags(self):
        self.test_client.post('/api/v2/auth/signup/',
                              data=json.dumps(self.user),
                              content_type='application/json')

        response = self.test_client.post('/api/v2/auth/login/',
                                         data=json.dumps(self.user),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        token = response_out['token']
        headers = {'Authorization': f'Bearer {token}'}

        response = self.test_client.post(
            '/api/v2/red-flags/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )
        response = self.test_client.get('/api/v2/red-flags/',
                                        content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('These are the recorded red-flags',
                      str(response_out['message']))

    def test_fetch_single_redflag(self):
        self.test_client.post('/api/v2/auth/signup/',
                              data=json.dumps(self.user),
                              content_type='application/json')

        response = self.test_client.post('/api/v2/auth/login/',
                                         data=json.dumps(self.user),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        token = response_out['token']
        headers = {'Authorization': f'Bearer {token}'}

        response = self.test_client.post(
            '/api/v2/red-flags/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )

        response = self.test_client.get('/api/v2/red-flags/1/',
                                        content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("red-flag details displayed",
                      str(response_out['message']))

    def test_add_redflag_without_token(self):
        response = self.test_client.post(
            '/api/v2/red-flags/',
            content_type='application/json',
            data=json.dumps(dict(
                createdBy="sankyu",
                location='123.01.56.78',
                image="image goes here",
                video="video goes here",
                comment="Policeman asked for something something"
            )))
        self.assertEqual(response.status_code, 401)
        self.assertIn("Missing Authorization Header", str(response.data))

    def test_delete_redflag(self):
        self.test_client.post('/api/v2/auth/signup/',
                              data=json.dumps(self.user),
                              content_type='application/json')

        response = self.test_client.post('/api/v2/auth/login/',
                                         data=json.dumps(self.user),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        token = response_out['token']
        headers = {'Authorization': f'Bearer {token}'}

        response = self.test_client.post(
            '/api/v2/red-flags/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )

        response = self.test_client.delete('/api/v2/red-flags/1/',
                                           content_type='application/json',)
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("This displayed red-flag has been deleted",
                      str(response_out['message']))

    def test_delete_redflag_nonexistent(self):
        response = self.test_client.delete('/api/v2/red-flags/10/',
                                           content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("redflag out of range, use valid id",
                      str(response_out['message']))