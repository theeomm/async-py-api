from fastapi.testclient import TestClient

from app.tests.fixtures import *


def test_new_todo(client: TestClient):
    """
    Test creating a new todo with the give note
    """
    note = "Happy testing"
    res = client.post(
        "/todos/",
        json={"note": note},
    )
    data = res.json()

    assert res.status_code == 200
    assert data["note"] == note
    assert data["id"] is not None


def test_new_todo_no_note(client: TestClient):
    """
    Throw error when there is no note provided
    """
    res = client.post(
        "/todos/",
        json={"note": None},
    )

    assert res.status_code == 422
