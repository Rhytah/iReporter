from reporter_api.views import incident_views, user_views
from flask import Flask, jsonify
from config import app_configuration
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from database.relations_commands import sqlcommands
from database.server import DatabaseConnect
from flask_cors import CORS


def create_app(mode):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(app_configuration)

        app.config['JWT_SECRET_KEY'] = 'super-secret'
        jwt = JWTManager(app)
        CORS(app)

        db = DatabaseConnect()
        for command in sqlcommands:
            db.cursor.execute(command)

        print(f"connection successful on {db.credentials}")
        from reporter_api.views.user_views import auth
        from reporter_api.views.incident_views import incident

        app.register_blueprint(auth)
        app.register_blueprint(incident)

    return app


app = create_app(mode='development')


@app.route('/')
def index():

    return jsonify({
        "message": "Welcome to iReporter API",
        "links": {
            "red-flags": "https://ireporter-backend-rhytah.herokuapp.com/api/v2/red-flags",
            "users": "https://ireporter-backend-rhytah.herokuapp.com/api/v2/auth/users",
            "intervention": "https://ireporter-backend-rhytah.herokuapp.comapi/v2/interventions"
        }
    })


@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify({
        "error": "You have made a bad request"
    }), 400


@app.errorhandler(500)
def handle_application_error(e):
    print(e)
    return jsonify({
        "error": "Something went wrong contact application admin"
    }), 500


@app.errorhandler(404)
def handle_notfound_error(e):
    return jsonify({
        "error": "You are trying to access a non exixtent url,\
        please check spelling and try again"
    }), 404


@app.errorhandler(405)
def handle_method_error(e):
    return jsonify({
        "error": "You tried to use a method not meant for resource,\
        please check and try again eith the right method"
    }), 405
