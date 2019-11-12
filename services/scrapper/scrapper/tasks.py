from __future__ import absolute_import, unicode_literals
from pydantic import BaseModel, ValidationError, validator
from scrapper.worker import app
from scrapper.models import Menu, MenuOrm, SportTypes


@app.task(bind=True, default_retry_delay=5)
def get_menu_soccer_from_betradar(self, data):
    data.update({"sport": SportTypes.SOCCER})
    try:
        obj = Menu(**data).create()
        return obj
    except ValidationError as e:
        print(e.json())


def update_soccer_menu(self):
    # run_menu_scrapper()
    pass
