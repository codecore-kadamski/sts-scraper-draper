from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery(
    "fetcher",
    # broker=settings.BROKER_URL,
    # broker=f'amqp://{settings.CELERY_LOGIN}:{settings.CELERY_PASS}@{settings.CELERY_HOST}:{settings.CELERY_PORT}',
    # backend='amqp://',
    include=["app.tasks"],
)
app.config_from_object("scrapper.celeryconfig")

# app.conf.update(
#     result_expires=3600,
#     CELERY_TASK_RESULT_EXPIRES=3600
# )


if __name__ == "__main__":
    app.start()
