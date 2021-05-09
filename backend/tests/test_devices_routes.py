from fastapi.testclient import TestClient

from app.main import api


client = TestClient(api)


def test_get_all_devices():
    response = client.get("/device/all")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_create_new_device():
    mock_device = {
        "name": "Mock device #1",
        "type": "Raspberry Pi",
        "description": "Mock device for testing"
    }

    response = client.post("/device", json=mock_device)
    response_json = response.json()

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    assert response_json["message"] == "Device successfully created"
    assert response_json["new device data"]["Device name"] == mock_device["name"]
    assert response_json["new device data"]["Device type"] == mock_device["type"]
    assert response_json["new device data"]["Device description"] == mock_device["description"]
