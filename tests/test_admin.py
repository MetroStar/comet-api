from fastapi.testclient import TestClient
from jose import jwt
from starlette import status

from app.main import app

client = TestClient(app)

SECRET_KEY = "secret"


def test_get_current_user():
    # Create a JWT token for testing
    payload = {"name": "Test User", "email": ""}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Test the endpoint
    response = client.get(
        "/api/current-user",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"user": payload}


def test_get_current_user_invalid_token():
    # Test the endpoint
    response = client.get(
        "/api/current-user",
        headers={"Authorization": "Bearer invalid_token"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Invalid JWT token"}
