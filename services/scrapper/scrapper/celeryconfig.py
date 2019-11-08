# config file for Celery Daemon
from celery.schedules import crontab
from scrapper import config

# default RabbitMQ broker
BROKER_URL = config.get("BROKER_URL")

# default RabbitMQ backend
CELERY_RESULT_BACKEND = "amqp://"

# TimeZone, this should be changed
CELERY_TIMEZONE = "Europe/Warsaw"

CELERY_TASK_RESULT_EXPIRES = 30

# CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'


CELERYBEAT_SCHEDULE = {"update-menu": {"task": "scrapper.tasks.update_soccer_menu", "schedule": crontab(minute="*/3")}}

# CELERYBEAT_SCHEDULE = {
#     'every-minute': {
#         'task': 'proj.tasks.add',
#         'schedule': crontab(minute='*/1'),
#         'args': (1,2),
#     },
# }
