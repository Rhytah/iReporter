from flask import Flask,jsonify
from config import app_configuration
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity


app=Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  
jwt = JWTManager(app)
JWT_ACCESS_TOKEN_EXPIRES = False
@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify({
        "status":400,
        "error":"You have made a bad request"
    })

@app.errorhandler(500)
def handle_application_error(e):
    return jsonify({
        "status":500,
        "error":"Something went wrong contact application admin"
    })

@app.errorhandler(404)
def handle_notfound_error(e):
    return jsonify({
        "status":404,
        "error":"You are trying to access a non exixtent url, please check spelling and try again"
    })

@app.errorhandler(405)
def handle_method_error(e):
    return jsonify({
        "status":405,
        "error":"You tried to use aq method not meant for resource, please check and try again eith the right method"
    })


from reporter_api.views import incident_views, user_views

