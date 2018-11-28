from tests.test_base import BaseTestCase
from reporter_api.views import incident_views
import json

redflags =[]
class IncidentTestCase(BaseTestCase):

    def test_fetch_all_redflags(self):
        response= self.app.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.incidents))
        self.assertEqual(response.status_code,200)
        
        

    def test_fetch_single_redflag(self):
        response= self.app.get('/api/v1/red-flags/1',data=json.dumps(self.incident))
        self.assertEqual(response.status_code,200)
        self.assertIn("red-flag", str(response.data))

    def test_add_redflag(self):
        response=self.app.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(dict(
                createdOn = "yesterday",
                createdBy = "sankyu",
                type = "red-flag",
                location = '123.01.56.78',
                status = "draft",
                image = "image goes here",
                video = "video goes here",
                comment = "Policeman asked for something something"
            )))
        redflags.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertIn(" ", str(response.data))
        self.assertTrue(len(redflags),2)
        self.assertNotEqual("No redflags found",str(response.data))
        