import pytest

base_date = "2021-01-01T00:00:00.000000"
base_user = {
    "id": 0,
    "user_id": "testuser",
    "first_name": "Test",
    "last_name": "User",
    "display_name": "Test User",
    "email": "testuser1@test.com",
    "is_active": True,
    "created": base_date,
    "created_by": "System Account",
    "modified": base_date,
    "modified_by": "System Account",
}


async def seed_data(client):
    client.post("/api/users/", json=base_user)


@pytest.mark.asyncio
async def test_create_user(client):
    response = client.post("/api/users/", json=base_user)
    response_json = response.json()
    response_json["created"] = base_date
    response_json["modified"] = base_date

    assert response.status_code == 201
    assert response_json == base_user


@pytest.mark.asyncio
async def test_get_all_users(client):
    await seed_data(client)
    response = client.get("/api/users")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_users_paged(client):
    await seed_data(client)
    response = client.get("/api/users?page_number=0&page_size=10")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_user(client):
    await seed_data(client)
    response = client.get("/api/users/0")
    response_json = response.json()
    response_json["created"] = base_date
    response_json["modified"] = base_date

    assert response.status_code == 200
    assert response_json == base_user


@pytest.mark.asyncio
async def test_update_user(client):
    await seed_data(client)
    updated_user = base_user.copy()
    updated_user["is_active"] = False

    response = client.put("/api/users/0", json=updated_user)
    response_json = response.json()
    response_json["created"] = base_date
    response_json["modified"] = base_date

    assert response.status_code == 200
    assert response_json == updated_user


@pytest.mark.asyncio
async def test_update_user_invalid_id(client):
    await seed_data(client)
    response = client.put("/api/users/-1", json=base_user)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_user(client):
    await seed_data(client)
    response = client.delete("/api/users/0")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_user_invalid_id(client):
    await seed_data(client)
    response = client.delete("/api/users/-1")
    assert response.status_code == 404
