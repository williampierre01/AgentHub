from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "AgentHub API"}


def test_read_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_unknown_route_returns_not_found() -> None:
    response = client.get("/unknown")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_read_agent_uses_default_query_value() -> None:
    response = client.get("/agents/7")

    assert response.status_code == 200
    assert response.json() == {
        "agent_id": 7,
        "include_status": False,
    }


def test_read_agent_converts_query_value() -> None:
    response = client.get("/agents/7?include_status=true")

    assert response.status_code == 200
    assert response.json() == {
        "agent_id": 7,
        "include_status": True,
    }


def test_read_agent_rejects_invalid_path_value() -> None:
    response = client.get("/agents/not-an-integer")

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["path", "agent_id"]
    assert response.json()["detail"][0]["type"] == "int_parsing"
