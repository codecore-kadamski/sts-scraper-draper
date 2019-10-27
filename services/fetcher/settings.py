import os

SOCCER_SPORT_CLASS = "sport-1"
CONTINENTS = [
    "Europa"
]  # , 'Ameryka Płn.', 'Ameryka Płd.', 'Afryka', 'Azja', 'Oceania', 'Świat'
SELECTORS = {
    "Europa": ("get_europe", ["A - G", "H - N", "P - W", "Młodzieżowe"]),
    "Ameryka Płn.": ("get_america_n", ["Wszystkie"]),
    "Ameryka Płd.": ("get_america_s", ["Wszystkie"]),
    "Afryka": ("get_africa", ["A - K", "M - S", "T - Z", "Młodzieżowe"]),
    "Afryka": ("get_asia", ["A - I", "J - M", "O - W", "Z - Z", "Młodzieżowe"]),
    "Oceania": ("get_oceania", ["Nowa Zelandia"]),
    "Świat": (
        "get_glob",
        ["Międzynarodowe", "Międzynarodowe Klubów", "Międzynarodowe Młodzieżowe"],
    ),
}
CLIENT_ID = 66
BETRADAR_URL = f"http://stats.betradar.com/s4/?clientid={CLIENT_ID}#"


CELERY_LOGIN = os.environ.get("CELERY_LOGIN")
CELERY_PASS = os.environ.get("CELERY_PASS")
CELERY_HOST = os.environ.get("CELERY_HOST")
CELERY_PORT = os.environ.get("CELERY_PORT")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_DB = os.environ.get("REDIS_DB")

BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
