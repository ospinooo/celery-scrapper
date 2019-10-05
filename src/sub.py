import datetime
import time
import tweepy

from twitter import api
from worker.app import process_tweet


class TwitterStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        print("data")
        process_tweet.delay(data)
        return True

    def on_error(self, status):
        print("err0r")


trends_stream = TwitterStreamListener(api=api)

stream = tweepy.Stream(
    auth=api.auth, listener=trends_stream)

stream.filter(track=['python'])
