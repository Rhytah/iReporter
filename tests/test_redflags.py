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
                lat=1.36564,
                long=32.66674,
                image="image goes here",
                video="video goes here",
                comment="Policeman asked for something something"
            )))
        self.assertEqual(response.status_code, 401)
        self.assertIn("Missing Authorization Header", str(response.data))

    def test_remove_redflag(self):
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
        self.assertIn("Redflag not found.",
                      str(response_out['message']))
    def test_modify_location(self):
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
        new_value=dict(lat=15.369,long=25.695)
        response = self.test_client.patch('/api/v2/red-flags/1/location',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("You have changed red flag's location to{'lat': 15.369, 'long': 25.695}",response_out['message'])
    
    def test_modify_comment(self):
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
        new_value=dict(comment="new_comment")
        response = self.test_client.patch('/api/v2/red-flags/1/comment',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("You have changed red flag's comment to{'comment': 'new_comment'}",response_out['message'])

    def test_modify_status(self):
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
        new_value=dict(status="resolved")
        response = self.test_client.patch('/api/v2/red-flags/1/status',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)
        self.assertIn('Missing Authorization Header',response_out['msg'])

    def test_admin_modify_status(self):
        credentials=dict(username='admin',password='sup3rpsW')
        response = self.test_client.post('/api/v2/auth/login/',
                                         data=json.dumps(credentials),
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
        new_value=dict(status="resolved")
        response = self.test_client.patch('/api/v2/red-flags/1/status',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)
        self.assertIn('Missing Authorization Header',response_out['msg'])