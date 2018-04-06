import requests
from flask import Flask, jsonify
from utils.log import Log

app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# Swagger(app, template_file='swagger/template.yml')

log = Log().get_logger(__name__)


@app.route("/", methods=["get"])
# @swag_from("swagger/proxy.yml")
def root():
    return jsonify(requests.get("http://127.0.0.1:8080/movies").json())
