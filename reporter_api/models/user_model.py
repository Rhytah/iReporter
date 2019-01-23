import datetime
from database.server import DatabaseConnect
from flask import jsonify

db = DatabaseConnect()


class User:
    
    def get_users(self):
        cmd = "SELECT * FROM users;"
        db.cursor.execute(cmd)
        all_users = db.cursor.fetchall()
        return all_users

    def create_user(self,firstname, lastname, username, password, email, phone_number):
        add_user_cmd = "INSERT INTO users(firstname,lastname, username, password, email,phone_number)\
       VALUES ('{}','{}','{}','{}','{}','{}');".format( firstname, lastname, username, password, email, phone_number)
        db.cursor.execute(add_user_cmd)


    def signup_search_user(self, email):
        cmd = "SELECT * FROM users WHERE email='{}'".format(email)
        db.cursor.execute(cmd)
        result = db.cursor.fetchone()
        if result:
            return jsonify({"status": 409,
                            "data": (email),
                            "error": "User already exists"})
    def login_search_user(self, username):
        cmd = "SELECT * FROM users WHERE username='{}'".format(username)
        db.cursor.execute(cmd)
        result = db.cursor.fetchone()
        return result