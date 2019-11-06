from enum import Enum, IntEnum
import pydantic as pd
from sqlalchemy.sql import func
from pydantic import BaseModel, Json, AnyUrl
from typing import Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
from datetime import date, datetime, time, timedelta

from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from app.database import session


Base = declarative_base()


class AutoLengthEnumField(Enum):
    def __init__(self, enum, **kwargs):
        max_length = (max(len(item.value) for item in enum) // 10 + 1) * 10
        kwargs.setdefault('max_length', max_length)
        super().__init__(enum, **kwargs)


class SportTypes(IntEnum):
    #SOCCER = (1, 'soccer', '2_1', 'Piłka Nożna')
    SOCCER = 1


class MenuOrm(Base):
    __tablename__ = 'fetcher_menu'
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