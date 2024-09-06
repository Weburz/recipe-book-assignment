# """The test suite for the root route."""

# from fastapi.testclient import TestClient


# class TestRootRoute:
#     """The class to group all test cases for the root route."""

#     def test_root_route_returns_status_200_ok(self, test_client: TestClient) -> None:
#         """Test whether the root route returns a status code 200 OK."""
#         with test_client as client:
#             response = client.get("/")
#             assert (
#                 response.status_code == 200
#             ), "The root route failed to return a status code 200 OK."
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_recipe():
    response = client.post("/recipes/", json={
        "id": 1,
        "name": "Pasta",
        "ingredients": ["pasta", "tomato sauce"],
        "instructions": "Boil pasta and add sauce."
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Pasta",
        "ingredients": ["pasta", "tomato sauce"],
        "instructions": "Boil pasta and add sauce."
    }

def test_get_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_recipe():
    response = client.get("/recipes/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Pasta"

def test_update_recipe():
    response = client.put("/recipes/1", json={
        "id": 1,
        "name": "Spaghetti",
        "ingredients": ["spaghetti", "tomato sauce"],
        "instructions": "Boil spaghetti and add sauce."
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Spaghetti"

def test_delete_recipe():
    response = client.delete("/recipes/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Recipe deleted"}
