FROM python:3.7-alpine3.8

EXPOSE 9000

RUN apk add --no-cache nginx uwsgi gcc libc-dev linux-headers bash
RUN pip install uwsgi

ADD nginx.conf /etc/nginx/conf.d
RUN mkdir /run/nginx

ENV LOGIN_SERVICE_HOST=""
ENV LOGIN_SERVICE_PORT=""
ENV MOVIE_SERVICE_HOST=""
ENV MOVIE_SERVICE_PORT=""
ENV WATCH_HISTORY_SERVICE_HOST=""
ENV WATCH_HISTORY_SERVICE_PORT=""

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /usr/local/src

ADD ./data ./data
ADD ./utils ./utils
ADD ./views ./views
ADD ./uwsgi.ini ./
ADD ./start.sh ./

CMD ["bash", "start.sh"]
