from flask import Flask, jsonify
from config import app_configuration
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from database.relations_commands import sqlcommands
from database.server import DatabaseConnect


def create_app(mode):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(app_configuration)

        app.config['JWT_SECRET_KEY'] = 'super-secret'
        jwt = JWTManager(app)

        # print(f"connection successful on {db.credentials}")
        from reporter_api.views.user_views import auth
        from reporter_api.views.incident_views import incident

        app.register_blueprint(auth)
        app.register_blueprint(incident)

    return app

app = create_app(mode='development')

@app.route('/')
def index():
    welcomemessage = """
    <!DOCTYPYE html>
    <html>
        <head>
        <title> iReporter API</title>

        </head>
        <body>
        <div class=maincontent>
            <h2>iReporter-API<h2>
            Currently supported endpoints
            <br>

            <a href='https://rhytah-ireporter.herokuapp.com/api/v2/red-flags'>
            Fetch all red-flags data
            </a>
            <br>
            <a href='https://rhytah-ireporter.herokuapp.com/api/v2/auth/users'>
            Fetch users
            </a>
            <br>
            <a href='https://rhytah-ireporter.herokuapp.com/api/v2/red-flags'>
            Fetch all intervention records
            </a>
            <br>
        </div>
        </body>
        </html>
    """
    return welcomemessage


@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify({
        "status": 400,
        "error": "You have made a bad request"
    })


@app.errorhandler(500)
def handle_application_error(e):
    return jsonify({
        "status": 500,
        "error": "Something went wrong contact application admin"
    })


@app.errorhandler(404)
def handle_notfound_error(e):
    return jsonify({
        "status": 404,
        "error": "You are trying to access a non exixtent url,\
        please check spelling and try again"
    })


@app.errorhandler(405)
def handle_method_error(e):
    return jsonify({
        "status": 405,
        "error": "You tried to use aq method not meant for resource,\
        please check and try again eith the right method"
    })

from reporter_api.views import incident_views, user_views