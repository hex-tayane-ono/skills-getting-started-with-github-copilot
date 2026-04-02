from fastapi.testclient import TestClient


def test_get_activities_status_code(client: TestClient):
    response = client.get("/activities")
    assert response.status_code == 200


def test_get_activities_returns_dict(client: TestClient):
    response = client.get("/activities")
    data = response.json()
    assert isinstance(data, dict)


def test_get_activities_structure(client: TestClient):
    response = client.get("/activities")
    activities = response.json()
    for name, activity in activities.items():
        assert "description" in activity, f"{name} missing 'description'"
        assert "schedule" in activity, f"{name} missing 'schedule'"
        assert "max_participants" in activity, f"{name} missing 'max_participants'"
        assert "participants" in activity, f"{name} missing 'participants'"
