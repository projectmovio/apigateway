import requests

from flask import Blueprint, jsonify
import utils.common as common

profile = Blueprint('login', __name__, url_prefix="")


@profile.route("/login", methods=["GET"])
def login():
    new_token = requests.get("http://127.0.0.1:8081/login").json()
    common.token_store.add_token(new_token)
    return jsonify(new_token)


