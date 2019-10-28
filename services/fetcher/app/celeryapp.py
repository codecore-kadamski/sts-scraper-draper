from __future__ import absolute_import, unicode_literals
from celery import Celery
from dynaconf import settings


app = Celery(
    'fetcher',
    # broker=settings.BROKER_URL,
    # broker=f'amqp://{settings.CELERY_LOGIN}:{settings.CELERY_PASS}@{settings.CELERY_HOST}:{settings.CELERY_PORT}',
    # backend='amqp://',
    include=['fetcher.tasks']
)
app.config_from_object('fetcher.celeryconfig')

app.conf.update(
    result_expires=3600,
    CELERY_TASK_RESULT_EXPIRES=3600
)
#app.autodiscover_tasks()


if __name__ == '__main__':
    app.start()
