import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, Dockerized Python!"

def test_echo(client):
    response = client.post("/echo", json={"foo": "bar"})
    assert response.status_code == 200
    assert response.json["you_sent"] == {"foo": "bar"}
