import json
import time
import random
from celery import Celery
from celery.schedules import crontab
from db import client

# Celery APP
app = Celery(
    'src.app',
    broker='redis://redis',
    # broker='redis://localhost',
    # backend='db+sqlite:///results.sqlite',
    # backend='redis://localhost',
)


# from db.mongo import client as mongo

@app.task(
    bind=True,  # first argument will be the task itself
    default_retry_delay=10,
    name='process_tweet')
def process_tweet(self, data):
    # Parse
    tweet: dict = json.loads(data)

    # Calculate the features we want to save.

    # Save
    # db = mongo["twitter"]
    # collection = db["tweets"]
    # collection.insert_one({
    #     'text': '',
    #     'hastags': ''})

    return tweet


@app.task(
    bind=True,
    default_retry_delay=10,
    name='scheduled')
def hola(self, a, b):
    print(a+b)
    return str(a+b)


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'exec': {
        'task': 'hola',
        'schedule': crontab(minute='*/1'),
        'args': (16, 16),
    },
}


# @task_postrun.connect()
# def task_postrun(signal=None, sender=None, task_id=None, task=None,
#                  args=None, kwargs=None, retval=None, state=None):
#     # For example we don't want to store info about specific tasks
#     ignored_tasks = ('tasks.ignore_task', )

#     if task.name not in ignored_tasks:
#         # write info about a finished task into SQLite
#         conn = sqlite3.connect('db')
#         conn.execute(
#             'INSERT INTO celery_tasks (task_id, task_name, state, created) VALUES (?,?,?,?)',
#             (task_id, task.name, state, datetime.now())
#         )

#         conn.commit()
#         conn.close()
