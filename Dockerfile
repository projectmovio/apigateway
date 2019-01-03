FROM python:3.7-alpine3.8

EXPOSE 9000

ENV LOGIN_SERVICE_HOST=""
ENV LOGIN_SERVICE_PORT=""
ENV MOVIE_SERVICE_HOST=""
ENV MOVIE_SERVICE_PORT=""
ENV WATCH_HISTORY_SERVICE_HOST=""
ENV WATCH_HISTORY_SERVICE_PORT=""

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . "/usr/local/src"
WORKDIR "/usr/local/src"

CMD ["python", "run_flask.py"]
