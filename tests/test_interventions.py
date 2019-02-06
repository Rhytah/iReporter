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
        self.assertIn("Intervention record not found.",res['error'])


    def test_add_intervention_without_token(self):
        response = self.test_client.post(
            '/api/v2/interventions/',
            content_type='application/json',
            data=json.dumps(dict(
                createdBy="sankyu",
                lat='01.556',
                long = '12.589',
                image="image goes here",
                video="video goes here",
                comment="Policeman asked for something something"
            )))
        self.assertEqual(response.status_code, 401)
        self.assertIn("Missing Authorization Header", str(response.data))

    def test_delete_an_intervention(self):
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

        response = self.test_client.delete('/api/v2/interventions/1/',
                                           content_type='application/json',)
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("This intervention has been deleted",
                      str(response_out['message']))

    def test_delete_out_of_range_intervention(self):
        response = self.test_client.delete('/api/v2/interventions/1/',
                                           content_type='application/json',)
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("Intervention record not found.",
                      str(response_out['error']))

    def test_modify_interventionlocation(self):
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
        new_value=dict(lat=15.369,long=25.695)
        response = self.test_client.patch('/api/v2/interventions/1/location',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("You have changed intervention's location",response_out['message'])
    
    def test_modify_interventionlocation_out_of_range(self):
        new_value=dict(lat=15.369,long=25.695)
        response = self.test_client.patch('/api/v2/interventions/1/location',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("Intervention record not found.",response_out['error']) 

    def test_modify_interventionlocation_invalid_data(self):
        new_value=dict(lat="15.369",long="25.695")
        response = self.test_client.patch('/api/v2/interventions/1/location',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('location must be a float value',response_out['error']) 
    
    def test_modify_interventionlocation_missing_data(self):
        new_value=dict(lat=15.369,long="")
        response = self.test_client.patch('/api/v2/interventions/1/location',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('location is missing',response_out['error']) 


    def test_modify_interventioncomment(self):
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
        new_value=dict(comment="new_comment")
        response = self.test_client.patch('/api/v2/interventions/1/comment',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("You have changed intervention's comment",response_out['message'])


    def test_modify_interventioncomment_invalid_datatype(self):
        new_value=dict(comment="roads")
        response = self.test_client.patch('/api/v2/interventions/1/comment',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Intervention record not found.',response_out['error']) 

    def test_modify_interventioncomment_invalid_data(self):
        new_value=dict(comment=456)
        response = self.test_client.patch('/api/v2/interventions/1/comment',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('comment must be a string',response_out['error']) 
    
    def test_modify_interventioncomment_missing_data(self):
        new_value=dict(comment="")
        response = self.test_client.patch('/api/v2/interventions/1/comment',
                                        content_type='application/json',
                                        data=json.dumps(new_value))
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('comment is missing',response_out['error']) 

