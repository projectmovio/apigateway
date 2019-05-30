import logging
import os

import requests

from flask import Blueprint, request, Response, jsonify

from utils.common import validate_user

log = logging.getLogger("apigateway.movies")

profile = Blueprint("movies", __name__, url_prefix="")

host = os.getenv("MOVIE_SERVICE_HOST", "localhost")
port = os.getenv("MOVIE_SERVICE_PORT", "8082")
url = "{}:{}".format(host, port)


@profile.route("/movies", methods=["GET"])
def movies():
    log.debug("Request: %s", request)
    log.debug("Headers: %s", request.headers)

    if not validate_user(request):
        return Response("{'Error': 'Unauthenticated'}", status=401, mimetype='application/json')

    return jsonify(requests.get("http://{}/movies".format(url), headers=request.headers).json())


