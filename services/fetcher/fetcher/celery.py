from __future__ import absolute_import
from celery import Celery
from dynaconf import settings


app = Celery(
    'fetcher',
    broker=f'amqp://{settings.CELERY_LOGIN}:{settings.CELERY_PASS}@{settings.CELERY_HOST}:{settings.CELERY_PORT}',
    backend='rpc://',
    include=['fetcher.tasks']
)
