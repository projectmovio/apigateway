FROM python:3.7-alpine3.8

EXPOSE 9000

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . "/usr/local/src"
WORKDIR "/usr/local/src"

CMD ["python", "run_flask.py"]
