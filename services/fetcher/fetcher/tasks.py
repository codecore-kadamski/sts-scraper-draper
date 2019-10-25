from __future__ import absolute_import
from fetcher.celery import app
# import time,requests
# from pymongo import MongoClient


# client = MongoClient('10.1.1.234', 27018) # change the ip and port to your mongo database's
# db = client.mongodb_test

# collection = db.celery_test
# post = db.test


@app.task(bind=True, default_retry_delay=10)  # set a retry delay, 10 equal to 10s
def fetch_data(self, obj):
    print(obj['calendar_url'])
