import logging
import os

import requests

from flask import Blueprint, request, Response

from utils.common import validate_user

log = logging.getLogger("apigateway.watch_history")

profile = Blueprint("watch_history", __name__, url_prefix="")

host = os.getenv("WATCH_HISTORY_SERVICE_HOST", "localhost")
port = os.getenv("WATCH_HISTORY_SERVICE_PORT", "8083")
url = "{}:{}".format(host, port)


@profile.route("/<user_id>/watch-history/<movie_id>", methods=["POST"])
def add_movie(user_id, movie_id):
    log.debug("Request: %s", request)

    if not validate_user(request):
        return Response("{'Error': 'Unauthenticated'}", status=401, mimetype='application/json')

    res = requests.post("http://{}/{}/watch-history/{}".format(url, user_id, movie_id),
                        headers=request.headers)

    return res.content, res.status_code, res.headers.items()
