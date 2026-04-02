from fastapi.testclient import TestClient


def test_signup_success(client: TestClient):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert email in data["message"]
    assert activity_name in data["message"]


def test_signup_unknown_activity(client: TestClient):
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 404


def test_signup_already_registered(client: TestClient):
    # Arrange — michael@mergington.edu is pre-seeded in Chess Club
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400
