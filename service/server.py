import requests
from flask import Flask, jsonify
from flask_cors import CORS

from utils.log import Log

app = Flask(__name__)
log = Log().get_logger(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["get"])
def root():
    return jsonify(requests.get("http://127.0.0.1:8080/movies").json())


@app.route("/login", methods=["get"])
def login():
    return jsonify(requests.get("http://127.0.0.1:8081/login").json())
