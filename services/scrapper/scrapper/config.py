# import os
from dynaconf import settings

SOCCER_SPORT_CLASS = "sport-1"
CONTINENTS = ["Europa"]  # , 'Ameryka Płn.', 'Ameryka Płd.', 'Afryka', 'Azja', 'Oceania', 'Świat'
SOCCER = {
    "Europa": ("get_europe", ["A - G", "H - N", "P - W", "Młodzieżowe"]),  # ["A - G", "H - N", "P - W", "Młodzieżowe"]
    "Ameryka Płn.": ("get_america_n", ["Wszystkie"]),
    "Ameryka Płd.": ("get_america_s", ["Wszystkie"]),
    "Afryka": ("get_africa", ["A - K", "M - S", "T - Z", "Młodzieżowe"]),
    "Afryka": ("get_asia", ["A - I", "J - M", "O - W", "Z - Z", "Młodzieżowe"]),
    "Oceania": ("get_oceania", ["Nowa Zelandia"]),
    "Świat": ("get_glob", ["Międzynarodowe", "Międzynarodowe Klubów", "Międzynarodowe Młodzieżowe"]),
}
CLIENT_ID = 66
BETRADAR_URL = f"http://stats.betradar.com/s4/?clientid={CLIENT_ID}#"
BROKER_URL = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"


# CELERY_LOGIN = os.environ.get("CELERY_LOGIN")
# CELERY_PASS = os.environ.get("CELERY_PASS")
# CELERY_HOST = os.environ.get("CELERY_HOST")
# CELERY_PORT = os.environ.get("CELERY_PORT")
#
# REDIS_HOST = os.environ.get("REDIS_HOST")
# REDIS_PORT = os.environ.get("REDIS_PORT")
# REDIS_DB = os.environ.get("REDIS_DB")
#
#
#
# MYSQL_ROOT_USER = os.environ.get("MYSQL_ROOT_USER")
# MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
# MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
# MYSQL_USER = os.environ.get("MYSQL_USER")
# MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
# MYSQL_ROOT_HOST = os.environ.get("MYSQL_ROOT_HOST")
# MYSQL_HOST = os.environ.get("MYSQL_HOST")

CELERY_LOGIN = settings.get("CELERY_LOGIN")
CELERY_PASS = settings.get("CELERY_PASS")
CELERY_HOST = settings.get("CELERY_HOST")
CELERY_PORT = settings.get("CELERY_PORT")

REDIS_HOST = settings.get("REDIS_HOST")
REDIS_PORT = settings.get("REDIS_PORT")
REDIS_DB = settings.get("REDIS_DB")


MYSQL_ROOT_USER = settings.get("MYSQL_ROOT_USER")
MYSQL_ROOT_PASSWORD = settings.get("MYSQL_ROOT_PASSWORD")
MYSQL_PASSWORD = settings.get("MYSQL_PASSWORD")
MYSQL_USER = settings.get("MYSQL_USER")
MYSQL_DATABASE = settings.get("MYSQL_DATABASE")
MYSQL_ROOT_HOST = settings.get("MYSQL_ROOT_HOST")
MYSQL_HOST = settings.get("MYSQL_HOST")
