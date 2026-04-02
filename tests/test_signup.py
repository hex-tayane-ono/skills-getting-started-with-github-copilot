from fastapi.testclient import TestClient


def test_signup_success(client: TestClient):
    response = client.post("/activities/Chess Club/signup?email=newstudent@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "newstudent@mergington.edu" in data["message"]
    assert "Chess Club" in data["message"]


def test_signup_unknown_activity(client: TestClient):
    response = client.post("/activities/Nonexistent Activity/signup?email=student@mergington.edu")
    assert response.status_code == 404


def test_signup_already_registered(client: TestClient):
    # michael@mergington.edu is pre-seeded in Chess Club
    response = client.post("/activities/Chess Club/signup?email=michael@mergington.edu")
    assert response.status_code == 400
