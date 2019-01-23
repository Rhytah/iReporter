from reporter_api import app
from tests.test_base import BaseTestCase
from reporter_api.views import incident_views
import json

from flask_jwt_extended import JWTManager, create_access_token


class IncidentTestCase(BaseTestCase):

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
            data=json.dumps(dict(
                location=[123.01, 110.36],
                image="image",
                video="image",
                comment="Bribery hhhhhhhki"
            )),
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
        response = self.test_client.delete('/api/v2/red-flags/1/',
                                           content_type='application/json',)
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("This displayed red-flag has been deleted",
                      str(response_out['message']))

    def test_delete_redflag_nonexistent(self):
        response = self.test_client.delete('/api/v2/red-flags/3/',
                                           content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("redflag out of range, use valid id",
                      str(response_out['message']))

    def test_edit_out_of_range_location(self):
        location_data = "new LatLong location"
        response = self.test_client.patch('/api/v2/red-flags/5/location/',
                                          data=json.dumps(location_data),
                                          content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Invalid id, try again", str(response.data))

    def test_edit_out_of_range_comment(self):

        data = "some new comment"
        response = self.test_client.patch('/api/v2/red-flags/20/comment/',
                                          data=json.dumps(data),
                                          content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Invalid id, try again", str(response.data))

    def test_edit_redflagstatus_without_token(self):
        data = "resolved"
        response = self.test_client.patch('/api/v2/red-flags/1/status/',
                                          data=json.dumps(data),
                                          content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(
            'b\'{\\n  "msg": "Missing Authorization Header"\\n}\\n\'', str(response.data))

    def test_edit_status_as_user(self):
        response = self.test_client.post('/api/v2/auth/login/',
                                         data=json.dumps(self.user),
                                         content_type='application/json')
        response_out = json.loads(response.data.decode())
        token = response_out['token']
        headers = {'Authorization': f'Bearer {token}'}
        new_status = "something"
        response2 = self.test_client.patch(
            '/api/v2/red-flags/1/status/',
            data=json.dumps(new_status),
            headers=headers,
            content_type='application/json'
        )
        response_out = json.loads(response2.data.decode())

        self.assertEqual(response_out['status'], 401)
        self.assertIsInstance(response_out, dict)
        self.assertIn(
            'Only admins can change status of a red-flag', str(response_out))

    def test_edit_status_as_admin(self):
        res = self.test_client.post('/api/v2/auth/login/',
                                    data=json.dumps(self.admin_user),
                                    content_type='application/json')
        response_out = json.loads(res.data.decode())
        token = response_out['token']
        headers = {'Authorization': f'Bearer {token}'}
        new_status = "something"
        response2 = self.test_client.patch(
            '/api/v2/red-flags/1/status/',
            data=json.dumps(new_status),
            headers=headers,
            content_type='application/json'
        )
        response_out = json.loads(response2.data.decode())
        self.assertEqual(response_out['status'], 400)
        self.assertIsInstance(response_out, dict)
        self.assertIn('Invalid id, try again', response_out['error'])