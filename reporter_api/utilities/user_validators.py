import re
from flask import jsonify


class UserValidator:
    def validate_add_user(self, firstname, lastname, username, email, password, phone_number, othernames):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return jsonify({"status": 400,
                            "error": "Use valid email address format. ...janedoe@int.com"
                            })
        if not firstname or firstname.isspace():
            return jsonify({
                "status": 400,
                "error": "firstname is missing"})
        if not lastname or lastname.isspace():
            return jsonify({
                "status": 400,
                "error": "lastname is missing"})
        if not othernames or othernames.isspace():
            return jsonify({
                "status": 400,
                "error": "othernames is missing"})
        if not re.match(r"^([a-zA-Z\d]+[-_])*[a-zA-Z\d*]+$", firstname) or not isinstance(firstname, str):
            return jsonify({
                "status": 400,
                "error": "firstname cannot be integers, have white spaces or symbols"
            })
        if not re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', password):
            return jsonify({
                "status": 400,
                "error": ["Password should be at least 6 characters long"
                          "uppercase letters: A-Z",
                          "lowercase letters- a-z",
                          "numbers: 0-9",
                          "any of the special characters: @#$%^&+="]
            })
        if not re.match(r"^([a-zA-Z\d]+[-_])*[a-zA-Z\d*]+$", username) or not isinstance(username, str):
            return jsonify({
                "status": 400,
                "error": "username cannot be integers,have white spaces or symbols"
            })
        if not re.match(r"^([a-zA-Z\d]+[-_])*[a-zA-Z\d*]+$", lastname) or not isinstance(lastname, str):
            return jsonify({
                "status": 400,
                "error": "lastname cannot be integers, have white spaces or symbols"
            })
        if not re.match(r"^([a-zA-Z\d]+[-_])*[a-zA-Z\d*]+$", othernames) or not isinstance(othernames, str):
            return jsonify({
                "status": 400,
                "error": "othernames cannot be integers, have white spaces or symbols"
            })
