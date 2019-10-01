from celery import Celery
# from scrapper.tasks import do_work
import time
import random

app = Celery(
    'scrapper',
    broker='redis://localhost'
)


@app.task(bind=True, default_retry_delay=10)
def do_work(self, item):
    print('Task received ' + str(item))
    # sleep for random seconds to simulate a really long task
    time.sleep(random.randint(1, 3))

    result = item + item
    return result
