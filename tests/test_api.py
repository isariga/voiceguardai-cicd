from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200

def test_predict():
    response = client.post("/predict")
    assert response.status_code == 200
    assert "label" in response.json()
    assert "confidence" in response.json()
