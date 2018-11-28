import unittest
from reporter_api import app

class BaseTestCase(unittest.TestCase):
   
    def setUp(self):
        self.app = app.test_client()
        self.incident=dict(
            
            createdOn = "10-12-2014",
            createdBy = "sankyu",
            type = "red-flag",
            location = '123.01.56.78',
            status = "draft",
            image = ["Image","Image"],
            video = ["Image","Image"],
            comment = "Policeman asked for something something"
            )
        self.incidents_empty = []
        self.incidents=[self.incident,self.incident]