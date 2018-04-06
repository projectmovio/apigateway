import requests
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from service.token_store import TokenStore
from utils.log import Log

app = Flask(__name__)
log = Log().get_logger(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

token_store = TokenStore()


@app.route("/login", methods=["get"])
def login():
    new_token = requests.get("http://127.0.0.1:8081/login").json()
    token_store.add_token(new_token)
    return jsonify(new_token)


@app.route("/movies", methods=["get"])
def movies():
    log.debug("Request: %s", request)
    log.debug("Headers: %s", request.headers)

    token = request.headers.get("user_id")
    log.debug("Token: %s", token)
    if token == "":
        log.debug("Empty token")
        return Response("{'Error': 'Empty Token'}", status=401, mimetype='application/json')

    valid = token_store.validate_token(token)
    if not valid:
        return Response("{'Error': 'Invalid Token'}", status=401, mimetype='application/json')
    return jsonify(requests.get("http://127.0.0.1:8082/movies", headers=request.headers).json())


