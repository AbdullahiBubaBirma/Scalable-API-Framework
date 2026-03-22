from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to the API"

def test_get_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 42
    assert data["name"] == "Item 42"

