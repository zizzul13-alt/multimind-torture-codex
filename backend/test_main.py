from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health_is_fastapi_proof():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "fastapi-benchmark-seam"

def test_session_contract_has_agent_truth():
    data = client.get("/api/session").json()
    assert data["id"] == "mm-2048"
    assert data["agents"][0]["state"] == "RUNNING"
