FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD ./src/ ./src/

EXPOSE 6379

WORKDIR src

ENTRYPOINT celery -A app worker --loglevel=info -E