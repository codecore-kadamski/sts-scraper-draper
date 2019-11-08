from datetime import date, datetime, time, timedelta
from enum import Enum, IntEnum
from typing import Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union

import pydantic as pd
from pydantic import AnyUrl, BaseModel, Json
from scrapper.database import session
from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class AutoLengthEnumField(Enum):
    def __init__(self, enum, **kwargs):
        max_length = (max(len(item.value) for item in enum) // 10 + 1) * 10
        kwargs.setdefault("max_length", max_length)
        super().__init__(enum, **kwargs)


class SportTypes(IntEnum):
    # SOCCER = (1, 'soccer', '2_1', 'Piłka Nożna')
    SOCCER = 1


class MenuOrm(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    sport = Column(Enum(SportTypes), default=None, nullable=True)
    continent = Column(String(), nullable=False)
    continent_url = Column(String(), nullable=False)
    country = Column(String(), nullable=False)
    country_url = Column(String(), nullable=False)
    league = Column(String(), nullable=False)
    league_url = Column(String(), nullable=False)
    summary_url = Column(String(), nullable=False, unique=True, index=True)
    calendar_url = Column(String(), nullable=False)
    sys_created = Column(DateTime(), server_default=func.now())
    sys_modified = Column(DateTime(), onupdate=func.now(), nullable=True)


class Menu(BaseModel):
    id: int = None
    sport: Optional[SportTypes] = None
    continent: str = None
    continent_url: AnyUrl = None
    country: str = None
    country_url: AnyUrl = None
    league: str = None
    league_url: AnyUrl = None
    summary_url: AnyUrl = None
    calendar_url: AnyUrl = None
    sys_created: datetime = datetime.now()
    sys_modified: datetime = None

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

    def create(self):
        data = self.dict()
        obj = MenuOrm(**data)
        session.add(obj)
        #  session.flush()
        session.commit()
        session.close()
        return obj


class MatchOrm(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    sport = Column(Enum(SportTypes), default=None, nullable=True)
    continent = Column(String(), nullable=False)
    continent_url = Column(String(), nullable=False)
    country = Column(String(), nullable=False)
    country_url = Column(String(), nullable=False)
    league = Column(String(), nullable=False)
    league_url = Column(String(), nullable=False)
    summary_url = Column(String(), nullable=False, unique=True, index=True)
    calendar_url = Column(String(), nullable=False)
    sys_created = Column(DateTime(), server_default=func.now())
    sys_modified = Column(DateTime(), onupdate=func.now(), nullable=True)


class Match(BaseModel):
    id: int = None
    league_id: int = None
    season: str = None
    league_id: int = None
    match_id: int = None
    match_url: AnyUrl = None
    match_date: datetime = None
    home_team: str = None
    visitors_team: str = None
    half_time: Optional[tuple] = ()
    full_time: Optional[tuple] = ()
    sys_created: datetime = datetime.now()
    sys_modified: datetime = None

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

    def create(self):
        data = self.dict()
        obj = MatchOrm(**data)
        session.add(obj)
        #  session.flush()
        session.commit()
        session.close()
        return obj

    # `id` INT NOT NULL AUTO_INCREMENT,
    # `league_id` INT NOT NULL,
    # `season` VARCHAR(100) DEFAULT NULL,
    # `match_id` INT NOT NULL, #19094606
    # `match_url` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL, #http://stats.betradar.com/s4/?clientid=66#2_1,3_257,22_1,5_66665,9_match,8_19094606,178_53064,7_5222
    # `match_date` TIMESTAMP DEFAULT NULL,
    # `match_time` TIMESTAMP DEFAULT NULL,
    # `home_team` VARCHAR(100) DEFAULT NULL,
    # `visitors_team` VARCHAR(100) DEFAULT NULL,
    # `half_time` VARCHAR(10) DEFAULT NULL,
    # `full_time` VARCHAR(10) DEFAULT NULL,
    # `sys_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    # `sys_modified` TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
