from fastapi.testclient import TestClient

from beerlog.api import api

client = TestClient(api)


def test_create_beer_via_api():
    response = client.post(
        "/beers",
        json={
            "name": "Skol",
            "style": "KornPA",
            "flavour": 1,
            "image": 1,
            "cost": 2,
        },
    )
    assert response.status_code == 200  # 201 return error
    result = response.json()
    assert result["name"] == "Skol"
    assert result["id"] == 1
