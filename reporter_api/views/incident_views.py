from flask import Flask, jsonify,request,json
from reporter_api import app
incident=dict(
    id=1,
    createdOn = "10-12-2014",
    createdBy = "sankyu",
    type = "red-flag",
    location = '123.01.56.78',
    status = "draft",
    Images = ["Image","Image"],
    videos = ["Image","Image"],
    comment = "Policeman asked for something something"
    )

@app.route('/api/v1/red-flags',methods=['GET'])
def fetch_red_flags():
    return "all red-flags"

@app.route('/api/v1/red-flags/<int:id>', methods = ['GET'])
def fetch_single_red_flag(id):
    return jsonify({"red-flag":incident})

@app.route('/api/v1/red-flags',methods=['POST'])
def add_red_flag():
    return "add logic to create record"