import json
from . import app
import time
import random

TWEET_FILTER = [
    'text',
    'time'
]


@app.task(bind=True, default_retry_delay=10)
def process_tweet(self, data):
    # Parse
    tweet: dict = json.loads(data)
    # Calculate the features we want to save.

    # Save

    return {k: v for k, v in tweet.values() if k in TWEET_FILTER}
