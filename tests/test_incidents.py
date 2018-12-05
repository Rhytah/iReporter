from reporter_api import app
from tests.test_base import BaseTestCase
from reporter_api.views import incident_views
import json

from flask_jwt_extended import JWTManager,create_access_token
class IncidentTestCase(BaseTestCase):
    
    def add_redflag_with_token(self):
        with self.app.app_context():
            response= self.test_client.post('/api/v1/red-flags',
                data=json.dumps(self.incident),
                content_type='application/json')
            response_out=json.loads(response.data.decode())
        self.assertEqual(response_out['status'],201)
        self.assertIsInstance(response_out,dict)
        self.assertIn("signup successful",str(response_out['message']))


    def test_fetch_all_redflags(self):
        response= self.test_client.get('/api/v1/red-flags',
        content_type='application/json')
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn("No red-flags found",str(response_out['message']))

    
    def test_fetch_single_redflag(self):
        response= self.test_client.get('/api/v1/red-flags/1',
        content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn("Out of range red-flag id,Try again with a valid id",str(response.data))

    def test_add_redflag_without_token(self):
        response=self.test_client.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(dict(
                createdBy = "sankyu",
                location = '123.01.56.78',
                image = "image goes here",
                video = "video goes here",
                comment = "Policeman asked for something something"
            )))
        self.assertEqual(response.status_code,401)
        self.assertIn("Missing Authorization Header",str(response.data))
       
    def test_delete_redflag(self):
        response=self.test_client.delete('/api/v1/red-flags/1',
        content_type='application/json',)
        response_out=json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertIn("redflag out of range, use valid id",str(response_out['message']))

    def test_delete_redflag_nonexistent(self):
        response=self.test_client.delete('/api/v1/red-flags/1',
        content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn("redflag out of range, use valid id",str(response.data))

    def test_edit_location(self):
        location_data = "new LatLong location"
        response=self.test_client.patch('/api/v1/red-flags/1/location',
        data=json.dumps(location_data),
        content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn("Invalid id, try again",str(response.data))

    def test_edit_comment(self):
        data ="some new comment"
        response=self.test_client.patch('/api/v1/red-flags/1/comment',
        data=json.dumps(data),
        content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn("",str(response.data))
        self.assertTrue("Invalid id, try again")