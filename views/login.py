import logging
import os

import requests

from flask import Blueprint, jsonify
import utils.common as common

log = logging.getLogger("apigateway.login")

profile = Blueprint('login', __name__, url_prefix="")

host = os.getenv("LOGIN_SERVICE_HOST", "localhost")
port = os.getenv("LOGIN_SERVICE_PORT", "8081")
url = "{}:{}".format(host, port)


@profile.route("/login", methods=["GET"])
def login():
    new_token = requests.get("http://{}/login".format(url)).json()
    common.token_store.add_token(new_token)
    return jsonify(new_token)


