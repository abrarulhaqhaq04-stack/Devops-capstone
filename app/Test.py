from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_todo():
    create_resp = client.post("/todos", json={"title": "Learn Docker", "done": False})
    assert create_resp.status_code == 200
    todo_id = create_resp.json()["id"]

    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Learn Docker"


def test_get_missing_todo():
    response = client.get("/todos/does-not-exist")
    assert response.status_code == 404