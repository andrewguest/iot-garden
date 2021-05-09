from fastapi.testclient import TestClient

from app.main import api


client = TestClient(api)


def test_system_update():
    response = client.get("/system/update")
    assert response.status_code == 200 or response.status_code == 304
