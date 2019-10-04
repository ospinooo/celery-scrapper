from twitter import _credentials
import tweepy

# Authentification
_auth = tweepy.OAuthHandler(
    _credentials.TWITTER_CONSUMER_API_KEY,
    _credentials.TWITTER_CONSUMER_API_SECRET_KEY)


_auth.set_access_token(
    _credentials.TWITTER_ACCESS_TOKEN,
    _credentials.TWITTER_ACCESS_SECRET_TOKEN)

api = tweepy.API(_auth)
