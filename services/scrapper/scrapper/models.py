# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey


from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()


class SportsOrm(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    sts_id = Column(Integer, nullable=False)
    name = Column(String(100), index=True, nullable=False, unique=True)
    url = Column(String(400), nullable=False, unique=True)


class Sports(BaseModel):
    id: int
    sts_id: int = None
    name: str(max_length=100) = None
    url: str(max_length=400) = None

    class Config:
        orm_mode = True
