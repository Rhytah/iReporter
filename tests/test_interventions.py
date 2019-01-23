from reporter_api import app
from tests.test_base import BaseTestCase
from reporter_api.views import incident_views
import json

from flask_jwt_extended import JWTManager, create_access_token


class IncidentTestCase(BaseTestCase):

    def test_add_intervention_with_token(self):

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
            '/api/v2/interventions/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )
        response_out = json.loads(response2.data.decode())
        print(response_out)
        self.assertEqual(response_out['status'], 201)
        self.assertIsInstance(response_out, dict)
        self.assertIn("Successfully added intervention",
                      str(response_out['message']))

    def test_fetch_interventions(self):
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
            '/api/v2/interventions/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )
        response = self.test_client.get('/api/v2/interventions/',
                                        content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('These are the Intervention records',
                      str(response_out['message']))

    def test_fetch_an_intervention(self):
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
            '/api/v2/interventions/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )

        response = self.test_client.get('/api/v2/interventions/1/',
                                        content_type='application/json')
    
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully fetched intervention record",str(response.data))
    def test_fetch_an_out_of_range_intervention(self):
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
            '/api/v2/interventions/',
            data=json.dumps(self.incident),
            headers=headers,
            content_type='application/json'
        )

        response = self.test_client.get('/api/v2/interventions/20/',
                                        content_type='application/json')
        res=json.loads(response.data.decode())
        self.assertEqual(res['status'], 404)
        self.assertIn("Invalid id. Try again with valid id",res['error'])


    def test_add_intervention_without_token(self):
        response = self.test_client.post(
            '/api/v2/interventions/',
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