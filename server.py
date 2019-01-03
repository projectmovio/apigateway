from flask import Flask
from flask_cors import CORS

from utils.log import Log
from views import login, movies, watch_history

app = Flask(__name__)
log = Log().get_logger("gateway")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(login.profile)
app.register_blueprint(movies.profile)
app.register_blueprint(watch_history.profile)











