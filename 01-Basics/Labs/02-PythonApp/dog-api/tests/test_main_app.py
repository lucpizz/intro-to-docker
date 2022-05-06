from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_main_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"success": "true"}


def test_get_route():
    response = client.get("/dogs/1")
    assert response.status_code == 200
    assert response.json() == {"dog_id": 1, "q": None}

def test_post_route():
    response = client.post("/dogs")
    assert response.status_code == 200
    assert response.json() == {"dog_id": 1, "q": None}


def test_put_route():
    response = client.post("/dogs")
    assert response.status_code == 200
    assert response.json() == {"dog_id": 1, "q": None}

def test_delete_route():
    response = client.delete("/dogs")
    assert response.status_code == 200
    assert response.json() == {"dog_id": 1, "q": None}