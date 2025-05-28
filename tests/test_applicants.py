base_applicant = {
    "id": 0,
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
    "created_at": "2023-10-01T00:00:00",
    "updated_at": "2023-10-01T00:00:00",
}


def test_create_applicant(client):
    response = client.post("/api/applicants/", json=base_applicant)
    assert response.status_code == 201
    assert response.json() == base_applicant


def test_get_all_applicants(client):
    response = client.get("/api/applicants")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_applicants_paged(client):
    response = client.get("/api/applicants?page_number=0&page_size=10")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_applicant(client):
    response = client.get("/api/applicants/0")
    assert response.status_code == 200
    assert response.json() == base_applicant


def test_update_applicant(client):
    updated_applicant = base_applicant.copy()
    updated_applicant["middle_name"] = "test"

    response = client.put("/api/applicants/0", json=updated_applicant)
    response_json = response.json()
    response_json["updated_at"] = updated_applicant["updated_at"]
    assert response.status_code == 200
    assert response_json == updated_applicant


def test_update_applicant_invalid_id(client):
    response = client.put("/api/applicants/-1", json=base_applicant)
    assert response.status_code == 404


def test_delete_applicant(client):
    response = client.delete("/api/applicants/0")
    assert response.status_code == 204


def test_delete_applicant_invalid_id(client):
    response = client.delete("/api/applicants/-1")
    assert response.status_code == 404
