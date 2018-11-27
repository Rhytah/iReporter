from tests.test_base import BaseTestCase
from reporter_api.views import incident_views
import json

redflags =[]
class IncidentTestCase(BaseTestCase):

    def test_fetch_all_redflags(self):
        response= self.app.get('/api/v1/red-flags')
        self.assertEqual(response.status_code,200)
        self.assertIn("all red-flags", str(response.data))
        

    def test_fetch_single_redflag(self):
        response= self.app.get('/api/v1/red-flags/1',data=json.dumps(self.incident))
        self.assertEqual(response.status_code,200)
        self.assertIn("red-flag", str(response.data))

    def test_add_redflag(self):
        response=self.app.post(
            '/api/v1/red-flags',
            data=json.dumps(dict(
                id=2,
                createdOn = "10-12-2014",
                createdBy = "sankyu",
                type = "red-flag",
                location = '123.01.56.78',
                status = "draft",
                Images = ["Image","Image"],
                videos = ["Image","Image"],
                comment = "Policeman asked for something something"
            )))
        redflags.append(dict)
        self.assertEqual(response.status_code,200)
        self.assertIn("add logic to create record", str(response.data))
        self.assertTrue(len(redflags),2)
        