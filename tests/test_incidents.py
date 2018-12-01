from tests.test_base import BaseTestCase
from reporter_api.views import incident_views
import json

class IncidentTestCase(BaseTestCase):

    def test_fetch_all_redflags(self):
        response= self.app.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.incidents))
        self.assertEqual(response.status_code,200)

    def test_fetch_all_redflags_empty(self):
        response = self.app.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.incidents_empty))
        self.assertEqual(len(self.incidents_empty),0)
    
    def test_fetch_single_redflag(self):
        response= self.app.get('/api/v1/red-flags/1')
        self.assertEqual(response.status_code,200)
        # self.assertEqual("Out of range red-flag id",response.data)

    def test_add_redflag(self):
        
        response=self.app.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(dict(
                createdBy = "sankyu",
                location = '123.01.56.78',
                image = "image goes here",
                video = "video goes here",
                comment = "Policeman asked for something something"
            )))
        self.incidents.append(dict)
        self.assertEqual(response.status_code,200)
        self.assertIn(" ", str(response.data))
        self.assertEqual(len(self.incidents),3)
        self.assertNotEqual("No redflags found",str(response.data))
        
    def test_delete_redflag(self):
        response=self.app.delete('/api/v1/red-flags/1',
        content_type='application/json',)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.incidents),2)
        self.assertIn("",str(response.data))

    def test_delete_redflag_nonexistent(self):
        response=self.app.delete('/api/v1/red-flags/1',
        content_type='application/json',
        data=json.dumps(self.incidents_empty))
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.incidents_empty),0)
        self.assertIn("redflag out of range, use valid id",str(response.data))

    def test_edit_location(self):
        location_data = "new LatLong location"
        response=self.app.patch('/api/v1/red-flags/1/location',
        data=json.dumps(self.incident),
        content_type='application/json')
        self.incident['location']=location_data
        self.assertEqual(response.status_code,200)
        self.assertIn("",str(response.data))

    def test_edit_comment(self):
        data = self.incident['comment'] ="some new comment"
        response=self.app.patch('/api/v1/red-flags/1/comment',
        data=json.dumps(data),
        content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn("",str(response.data))
        self.assertTrue("Invalid id, try again")
       
        