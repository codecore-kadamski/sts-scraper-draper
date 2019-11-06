from __future__ import absolute_import, unicode_literals
from app.celeryapp import app
from app.models import Menu, MenuOrm, SportTypes
from pydantic import BaseModel, ValidationError, validator


@app.task(bind=True, default_retry_delay=10)
def get_menu_soccer_from_betradar(self, data):
    data.update({
        'sport': SportTypes.SOCCER,
    })
    try:
        obj = Menu(**data).create()
        return obj
    except ValidationError as e:
        print(e.json())
