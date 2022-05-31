from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class BeerOut(BaseModel):
    id: int
    name: str
    style: str
    flavour: int
    image: int
    cost: int
    rate: int
    date: datetime


class BeerIn(BaseModel):
    id: int
    name: str
    style: str
    flavour: int
    image: int
    cost: int

    @validator("image", "flavour", "cost")
    def validate_ratings(cls, value, field):
        if value < 1 or value > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return value
