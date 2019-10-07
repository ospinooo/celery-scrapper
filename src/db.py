import pymongo
import os


MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_HOST = os.environ.get("MONGODB_HOST")

# client = pymongo.MongoClient(
#     f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}/admin?retryWrites=true&w=majority")

client = pymongo.MongoClient(
    f"mongodb://mongo:27017")

db = client.twitter
tweets = db.tweets
