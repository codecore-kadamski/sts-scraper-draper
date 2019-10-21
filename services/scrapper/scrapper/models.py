from typing import List
from pydantic import BaseModel, Field, constr
from pydantic.dataclasses import dataclass
from objects import (
    SportOrm,
)


@dataclass(config=SportOrm)
class Sport(BaseModel):
    id: int
    sts_id: int = Field(title='sts id')
    name: str = Field(title="Name of sport", max_length=100)
    url: str = Field(max_length=400, title='url')

    class Config:
        orm_mode = True

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return "%s" % self.name