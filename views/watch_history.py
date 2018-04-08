import requests

from flask import Blueprint, request, Response

from utils.common import validate_user
from utils.log import Log

log = Log().get_logger("gateway.watch_history")
profile = Blueprint("watch_history", __name__, url_prefix="")


@profile.route("/<user_id>/watch-history/<movie_id>", methods=["POST"])
def add_movie(user_id, movie_id):
    log.debug("Request: %s", request)

    if not validate_user(request):
        return Response("{'Error': 'Unauthenticated'}", status=401, mimetype='application/json')

    res = requests.post("http://127.0.0.1:8083/{}/watch-history/{}".format(user_id, movie_id),
                        headers=request.headers)

    return res.content, res.status_code, res.headers.items()
