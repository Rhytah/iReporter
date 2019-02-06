import unittest
from reporter_api import create_app
import json
import datetime
from database.server import DatabaseConnect
from database.relations_commands import sqlcommands

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app=create_app(mode='testing')
        with app.app_context():
            self.app = app
            self.test_client = self.app.test_client()
            self.db = DatabaseConnect()
            self.incident = dict(
                created_on="2019-01-23 12:21:56.983689",
                location=123.01,
                image="image",
                video="image",
                comment="Policeman asked for something something"
            )

            self.user = dict(
                firstname="sunny",
                lastname="tamale",
                othernames="funny",
                email="johndoe@gmail.com",
                phone_number=25678924556,
                username="sunnyk",
                password="pass1236"
            )

            self.testuser1 = dict(
                lastname="tamale",
                othernames="funny",
                email="johndoe@gmail.com",
                phone_number=25678924556,
                username="username",
                password="pass1236"

            )
            self.testuser2 = dict(
                firstname="sunny",
                othernames="funny",
                email="johndoe@gmail.com",
                phone_number=25678924556,
                username="username",
                password="pass1236"

            )
            self.testuser3 = dict(
                firstname="sunny",
                lastname="tamale",
                email="johndoe@gmail.com",
                phone_number=25678924556,
                username="username",
                password="pass1236"
            )

            self.testuser4 = dict(
                firstname="sunny",
                lastname="tamale",
                othernames="funny",
                email="someemail",
                phone_number=25678924556,
                username="username",
                password="pass1236"
            )

            self.testuser5 = dict(
                firstname="sunny",
                lastname="tamale",
                othernames="funny",
                phone_number=25678924556,
                username="username",
                password="pass1236"
            )
            self.reporter = dict(username='sunnyk', password='pass1236')
            self.admin_user = dict(firstname='Rhytah',lastname='Namono',othernames='Nadia',username='admin',password='sup3rpsW',\
            email='girl@world.com',phone_number=8562438 ,isadmin=True)

    def tearDown(self):
        self.db.drop_table('redflags')
        self.db.drop_table('users')
        self.db.drop_table('interventions')
        for command in sqlcommands:
            self.db.cursor.execute(command)