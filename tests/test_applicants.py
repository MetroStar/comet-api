import pytest

from tests.conftest import generalize_json_data

base_applicant = {
    "first_name": "John",
    "last_name": "Doe",
    "middle_name": "A",
    "gender": "M",
    "date_of_birth": "2023-01-01",
    "ssn": "023456789",
    "email": "john@test.com",
    "home_phone": "123-456-7890",
    "mobile_phone": "098-765-4321",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345",
    "country": "USA",
}


async def seed_data(client):
    client.post("/api/applicants/", json=base_applicant)


@pytest.mark.asyncio
async def test_create_applicant(client):
    response = client.post("/api/applicants/", json=base_applicant)
    response_json = generalize_json_data(response.json())
    assert response.status_code == 201
    assert response_json == base_applicant


@pytest.mark.asyncio
async def test_get_all_applicants(client):
    await seed_data(client)
    response = client.get("/api/applicants")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_applicants_paged(client):
    await seed_data(client)
    response = client.get("/api/applicants?page_number=0&page_size=10")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_applicant(client):
    await seed_data(client)
    response = client.get("/api/applicants/1")
    response_json = generalize_json_data(response.json())
    assert response.status_code == 200
    assert response_json == base_applicant


@pytest.mark.asyncio
async def test_update_applicant(client):
    await seed_data(client)
    updated_applicant = base_applicant.copy()
    updated_applicant["middle_name"] = "test"

    response = client.put("/api/applicants/1", json=updated_applicant)
    response_json = generalize_json_data(response.json())
    assert response.status_code == 200
    assert response_json == updated_applicant


@pytest.mark.asyncio
async def test_update_applicant_invalid_id(client):
    await seed_data(client)
    response = client.put("/api/applicants/-1", json=base_applicant)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_applicant(client):
    await seed_data(client)
    response = client.delete("/api/applicants/1")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_applicant_invalid_id(client):
    await seed_data(client)
    response = client.delete("/api/applicants/-1")
    assert response.status_code == 404
