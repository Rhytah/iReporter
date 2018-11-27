from flask import Flask
from config import app_configuration

app=Flask(__name__)


from reporter_api.views import incident_views

