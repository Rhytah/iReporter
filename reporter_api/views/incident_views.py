from flask import Flask, jsonify,request,json
from reporter_api import app
from reporter_api.controllers.incidents_controllers import IncidentsController

incidents_controller=IncidentsController()
@app.route('/api/v1/red-flags',methods=['GET'])
def fetch_red_flags():
    return "all red-flags"

@app.route('/api/v1/red-flags/<int:id>', methods = ['GET'])
def fetch_single_red_flag(id):
    return jsonify({"red-flag":"value of red flag here"})

@app.route('/api/v1/red-flags',methods=['POST'])
def add_red_flag():
    request_data=request.get_json()
    return incidents_controller.add_redflag(request_data)