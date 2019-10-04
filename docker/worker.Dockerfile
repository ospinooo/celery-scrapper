FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD ./src /src

ENTRYPOINT celery -A src.worker worker --concurrency=5 --loglevel=info