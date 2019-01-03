# Requirements
* python3.7
* pip install -r requirements.txt

# Start server

* `python run_flask.py`
* API base URL: `http://localhost:9000/`

# Run in Docker
* `docker build -t apigateway:latest .`
* `docker run -it -p 9000:9000 apigateway:latest`