import unittest
from reporter_api import app

class BaseTestCase(unittest.TestCase):
   
    def setUp(self):
        self.app = app.test_client()
        self.incident=dict(
            id=1,
            createdOn = "10-12-2014",
            createdBy = "sankyu",
            type = "red-flag",
            location = '123.01.56.78',
            status = "draft",
            Images = ["Image","Image"],
            videos = ["Image","Image"],
            comment = "Policeman asked for something something"
            )