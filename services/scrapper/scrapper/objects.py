from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SportOrm(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True, nullable=False)
    sts_id = Column(Integer, index=True, nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    url = Column(String(400), nullable=False, unique=True)
