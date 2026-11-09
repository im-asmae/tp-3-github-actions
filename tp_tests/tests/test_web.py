import pytest
from app.web import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_web_autorise(client):

    result = client.post("/moderate", json={"message": "bonjour"})
    #assert
    assert result.status_code==200
    assert result.get_json() == {"decision" : "autoriser"}

def test_web_bloque(client):

    result = client.post("/moderate", json={"message": "ceci est un SPAM"})
    #assert
    assert result.status_code==200
    assert result.get_json() == {"decision" : "bloquer"}

def test_web_vide(client):

    result = client.post("/moderate")
    #assert
    assert result.status_code==400
    assert result.get_json() == {"error" : "JSON object required"}

def test_web_invalide(client):

    result = client.post("/moderate", json={"message" : 42})
    #assert
    assert result.status_code==400
    assert result.get_json() == {"error" : "Invalid message"}

def test_web_str_vide(client):

    result = client.post("/moderate", json={"message" : " "})
    #assert
    assert result.status_code==400
    assert result.get_json() == {"error" : "Invalid message"}

def test_web_liste(client):

    result = client.post("/moderate", json=[])
    #assert
    assert result.status_code==400
    assert result.get_json() == {"error" : "JSON object required"}