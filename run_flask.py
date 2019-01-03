import os

from subprocess import Popen

os.environ["FLASK_APP"] = "server.py"
flask_ps = Popen(["flask", "run", "--host=0.0.0.0", "--port=9000", "--with-threads"])
flask_ps.communicate()