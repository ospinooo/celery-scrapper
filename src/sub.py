import datetime
import time
import tweepy

from twitter import api
from worker.tasks import process_tweet


class TwitterStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


trends_stream = TwitterStreamListener(api=api)

stream = tweepy.Stream(
    auth=api.auth, listener=trends_stream)

stream.filter(track=['python'])
