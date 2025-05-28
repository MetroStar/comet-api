base_case = {
    "id": 0,
    "status": "Not Started",
    "assigned_to": "Test User",
    "created_at": "2023-10-01T00:00:00",
    "updated_at": "2023-10-01T00:00:00",
    "applicant_id": 0,
}

base_case_with_applicant = {
    "id": 0,
    "status": "Not Started",
    "assigned_to": "Test User",
    "created_at": "2023-10-01T00:00:00",
    "updated_at": "2023-10-01T00:00:00",
    "applicant": None,  # This will be None if no applicant is associated
}


def test_create_case(client):
    response = client.post("/api/cases/", json=base_case)
    assert response.status_code == 201
    assert response.json() == base_case


def test_get_all_cases(client):
    response = client.get("/api/cases")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_cases_paged(client):
    response = client.get("/api/cases?page_number=0&page_size=10")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_cases(client):
    response = client.get("/api/cases/0")
    assert response.status_code == 200
    assert response.json() == base_case_with_applicant


def test_update_case(client):
    updated_case = base_case.copy()
    updated_case["assigned_to"] = "test user"

    response = client.put("/api/cases/0", json=updated_case)
    response_json = response.json()
    response_json["updated_at"] = updated_case["updated_at"]
    assert response.status_code == 200
    assert response_json == updated_case


def test_update_case_invalid_id(client):
    response = client.put("/api/cases/-1", json=base_case)
    assert response.status_code == 404


def test_delete_case(client):
    response = client.delete("/api/cases/0")
    assert response.status_code == 204


def test_delete_case_invalid_id(client):
    response = client.delete("/api/cases/-1")
    assert response.status_code == 404
