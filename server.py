import logging

from flask import Flask
from flask_cors import CORS

from views import login, movies, watch_history

log = logging.getLogger("apigateway")
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("urllib3").setLevel("WARNING")

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(login.profile)
app.register_blueprint(movies.profile)
app.register_blueprint(watch_history.profile)











