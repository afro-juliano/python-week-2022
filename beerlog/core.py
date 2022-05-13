from typing import Optional, List
from sqlmodel import select
from beerlog.database import get_session
from beerlog.models import Beer


def add_beer_to_database(
    name: str,
    style: str,
    flavour: int,
    image: int,
    cost: int,
) -> bool:
    with get_session() as session:
        beer = Beer(
            name=name,
            style=style,
            flavour=flavour,
            image=image,
            cost=cost
        )
        session.add(beer)
        session.commit()
    return True


def get_beers_from_database(style: Optional[str] = None) -> List[Beer]:
    with get_session() as session:
        sql = select(Beer)
        return list(session.exec(sql))
