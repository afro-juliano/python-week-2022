from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator
from statistics import mean
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavour: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavour", "image", "cost")
    def validate_ratings(cls, value, field):
        if value < 1 or value > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return value

    @validator("rate", always=True)
    def calculate_rate(cls, value, values):
        rate = mean([values["flavour"], values["image"], values["cost"]])
        return int(rate)


brewdog = Beer(name="Brewdog", style="NEIPA", flavour=6, image=8, cost=8)
