import random
import time
import json
from celery import Celery
# Create the celery app for the workers
app = Celery(
    'src.worker.app',
    broker='redis://redis',
    # backend='redis://localhost',
)


TWEET_FILTER = [
    'text',
    'time'
]


@app.task(bind=True, default_retry_delay=10, name='process_tweet')
def process_tweet(self, data):
    # Parse
    tweet: dict = json.loads(data)
    # Calculate the features we want to save.

    # Save

    return True
