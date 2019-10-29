import enum
import pydantic as pd
from pydantic import BaseModel, Json, AnyUrl
from datetime import date, datetime, time, timedelta

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class MenuSports(str, enum.Enum):
    SOCCER = ('soccer', '2_1', 'Piłka Nożna')


class Menu(BaseModel):
    id: int
    sport: MenuSports
    json: Json
    continent: str
    continent_url: AnyUrl
    country: str
    country_url: AnyUrl
    league: str
    league_url: AnyUrl
    summary_url: AnyUrl
    calendar_url: AnyUrl
    sys_created: date
    sys_modified: date
