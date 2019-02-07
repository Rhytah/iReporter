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

    def get_user(self, userid):
        cmd = "SELECT * FROM users WHERE userid='{}';".format(userid)
        db.cursor.execute(cmd)
        user = db.cursor.fetchone()
        return user

    def create_user(self, firstname, lastname, username, password, email):
        add_user_cmd = "INSERT INTO users(firstname,lastname, username, password, email)\
       VALUES ('{}','{}','{}','{}','{}') RETURNING email;".format(firstname, lastname, username, password, email)
        db.cursor.execute(add_user_cmd)
        return db.cursor.fetchone()

    def signup_search_user(self, email):
        cmd = "SELECT * FROM users WHERE email='{}'".format(email)
        db.cursor.execute(cmd)
        result = db.cursor.fetchone()
        if result:
            return jsonify({
                "error": (email)+"  User already exists"}), 409

    def login_search_user(self, username):
        cmd = f"SELECT * FROM users WHERE username='{username}';"
        db.cursor.execute(cmd)
        return db.cursor.fetchone()
