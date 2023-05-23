from unittest.mock import MagicMock, patch, AsyncMock

import pytest

from src.database.models import User
from src.services.auth import auth_service

CAT = {
    "nick": "Basilar",
    "age": 4,
    "vaccinated": False,
    "description": "Це дуже багато коду",
}


@pytest.fixture()
def token(client, user, session, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    client.post("/api/auth/signup", json=user)
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    current_user.role = "admin"
    session.commit()
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    data = response.json()
    return data["access_token"]


def test_create_cat(client, token):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        owner = client.post("api/owners", json={"email": "test@test.api.com"},
                            headers={"Authorization": f"Bearer {token}"})
        data = owner.json()
        owner_id = data["id"]
        CAT["owner_id"] = owner_id
        response = client.post("api/cats", json=CAT,
                               headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 201, response.text
        data = response.json()
        assert "id" in data
        assert CAT["nick"] == data["nick"]


def test_get_cat(client, token, monkeypatch):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.redis', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.identifier', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.http_callback', AsyncMock())
        response = client.get("api/cats", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200, response.text
        data = response.json()
        assert type(data) == list
        assert "id" in data[0]
        assert CAT["nick"] == data[0]["nick"]
