from flask import Flask
from config import app_configuration
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity


app=Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  
jwt = JWTManager(app)


from reporter_api.views import incident_views, user_views

