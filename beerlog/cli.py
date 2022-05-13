import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database


main = typer.Typer(help="Beer Management Application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavour: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database"""
    if add_beer_to_database(name, style, flavour, image, cost):
        print("Beer added to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database"""
    beers = get_beers_from_database(style)
    print(beers)
