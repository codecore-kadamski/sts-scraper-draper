

SOCCER_SPORT_CLASS = 'sport-1'
CONTINENTS = ['Europa', 'Ameryka Płn.', 'Ameryka Płd.', 'Afryka', 'Azja', 'Oceania', 'Świat']
SELECTORS = {
    'Europa': ('get_europe', ["A - G", "H - N", "P - W", "Młodzieżowe"],),
    'Ameryka Płn.': ('get_america_n', ["Wszystkie"],),
    'Ameryka Płd.': ('get_america_s', ["Wszystkie"],),
    'Afryka': ('get_africa', ["A - K", "M - S", "T - Z", "Młodzieżowe"],),
    'Afryka': ('get_asia', ["A - I", "J - M", "O - W", "Z - Z", "Młodzieżowe"],),
    'Oceania': ('get_oceania', ["Nowa Zelandia"],),
    'Świat': ('get_glob', ["Międzynarodowe", "Międzynarodowe Klubów", "Międzynarodowe Młodzieżowe"],),
}
CLIENT_ID = 66
BETRADAR_URL = f"http://stats.betradar.com/s4/?clientid={CLIENT_ID}#"


CELERY_LOGIN = os.env.get('CELERY_LOGIN')
CELERY_PASS = os.env.get('CELERY_PASS')
CELERY_HOST = os.env.get('CELERY_HOST')
CELERY_PORT = os.env.get('CELERY_PORT')
