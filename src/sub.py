import datetime
import time
import tweepy

from twitter import api
from app import process_tweet


class TwitterStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        print("data")
        process_tweet.delay(data)
        return True

    def on_error(self, status):

        if status == 420:
            print("Rate limit exceeded")


trends_stream = TwitterStreamListener()

stream = tweepy.Stream(
    auth=api.auth,
    listener=trends_stream)

stream.filter(track=['python'])
