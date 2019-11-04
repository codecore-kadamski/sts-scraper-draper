from __future__ import absolute_import, unicode_literals
from app.celeryapp import app

# import time,requests
# from pymongo import MongoClient


# client = MongoClient('10.1.1.234', 27018) # change the ip and port to your mongo database's
# db = client.mongodb_test

# collection = db.celery_test
# post = db.test

# @app.task(bind=True, default_retry_delay=10)  # set a retry delay, 10 equal to 10s
# def fetch_data(self, obj):
#     if obj:
#         print(obj['calendar_url'])

@app.task(bind=True, default_retry_delay=10)  # set a retry delay, 10 equal to 10s
def fetch_data(self, obj):
    if obj:
        print(obj['calendar_url'])


@app.task(bind=True, default_retry_delay=10)
def get_menu_soccer_from_betradar(urls):
    pass

# {
#     'continent': 'Europa',
#     'continent_url':
#     {
#         'part': '2_1,22_1'
#     },
#     'country': 'Wyspy Owcze',
#     'country_url':
#     {
#         'part': '2_1,3_201,22_1'
#     },
#     'league': 'Logmanssteypid',
#     'league_url':
#     {
#         'seasonid': '66655'
#     },
#     'summary_url': 'http://stats.betradar.com/s4/?clientid=66#2_1,3_201,22_1,5_66655,9_summary',
#     'calendar_url': 'http://stats.betradar.com/s4/?clientid=66#2_1,3_201,22_1,5_66655,9_fixtures,231_full,23_3'
# }