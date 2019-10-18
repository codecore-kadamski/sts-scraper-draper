import datetime

#from enum import Enum
import enum
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Enum

from .mixins import ActiveRecordsMixin, Base


class SportOption(enum.Enum):
    TENIS = 185
    FOOTBALL = 184
    BASKETBALL = 186
    SPECIALS = 201


class RegionOption(enum.Enum):
    POLAND = 6502
    ENGLAND = 6521
    FRANCE = 6535
    SPAIN = 6488
    GERMANY = 6482


class LeagueOption(enum.Enum):
    pass


class WinOption(enum.Enum):
    WIN1 = 1
    WIN1DRAW = 2
    DRAW = 3
    WIN2DRAW = 4
    WIN2 = 5
    BREAK = 6
    FUTURE = 7


class MatchTypeMixin:

    type_sport = Column(Enum(SportOption), default='', nullable=True)
    type_region = Column(Enum(RegionOption), default='', nullable=True)
    type_league = Column(Enum(LeagueOption), default='', nullable=True)


class BaseModel(ActiveRecordsMixin, MatchTypeMixin):
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)


class Match(BaseModel):
    __tablename__ = 'matchs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_match = Column(Integer)
    date = Column(DateTime, index=False, nullable=False)
    url = Column(String)
    expired = Column(Boolean, default=False)
    result = Column(Enum(WinOption), default='', nullable=False)
    content_data = Column(String, default={})
    score = Column(String(20))

    def __init__(self, id_match, date, url, expired, result, score, content_data):
        self.id_match = id_match
        # self.created = datetime.datetime.now()
        self.date = date
        self.url = url
        self.expired = expired
        self.result = result
        self.score = score
        self.content_data = content_data
