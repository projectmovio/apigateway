import requests

from flask import Blueprint, request, Response, jsonify

from utils.common import validate_user
from utils.log import Log

log = Log().get_logger("gateway.movies")
profile = Blueprint("movies", __name__, url_prefix="")


@profile.route("/movies", methods=["GET"])
def movies():
    log.debug("Request: %s", request)
    log.debug("Headers: %s", request.headers)

    if not validate_user(request):
        return Response("{'Error': 'Unauthenticated'}", status=401, mimetype='application/json')

    return jsonify(requests.get("http://127.0.0.1:8082/movies", headers=request.headers).json())


