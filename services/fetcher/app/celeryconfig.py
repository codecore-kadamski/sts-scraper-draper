# config file for Celery Daemon
from celery.schedules import crontab
from dynaconf import settings

# default RabbitMQ broker
BROKER_URL = settings.BROKER_URL

# default RabbitMQ backend
CELERY_RESULT_BACKEND = 'amqp://'

# TimeZone, this should be changed
CELERY_TIMEZONE = 'Europe/Warsaw'

# CELERYBEAT_SCHEDULE = {
#     'every-minute': {
#         'task': 'proj.tasks.add',
#         'schedule': crontab(minute='*/1'),
#         'args': (1,2),
#     },
# }
