from fastapi.testclient import TestClient


def test_get_activities_status_code(client: TestClient):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_dict(client: TestClient):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)
    data = response.json()

    # Assert
    assert isinstance(data, dict)


def test_get_activities_structure(client: TestClient):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for name, activity in activities.items():
        for key in expected_keys:
            assert key in activity, f"{name} missing '{key}'"
