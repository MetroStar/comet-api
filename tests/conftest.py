import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    yield client


def generalize_json_data(data):
    """
    Helper function to generalize JSON data for testing by removing
    auto-generated fields like id, created_at, updated_at.
    """
    new_data = data.copy()
    new_data.pop("id", None)
    new_data.pop("created_at", None)
    new_data.pop("updated_at", None)
    return new_data
