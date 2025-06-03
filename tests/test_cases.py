from tests.conftest import generalize_json_data

base_case = {
    "status": "Not Started",
    "assigned_to": "Test User",
    "applicant_id": 0,
}


def test_create_case(client):
    response = client.post("/api/cases/", json=base_case)
    response_json = generalize_json_data(response.json())
    assert response.status_code == 201
    assert response_json == base_case


def test_get_all_cases(client):
    response = client.get("/api/cases")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_cases_paged(client):
    response = client.get("/api/cases?page_number=0&page_size=10")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_case(client):
    response = client.get("/api/cases/1")
    response_json = generalize_json_data(response.json())
    response_json["applicant_id"] = 0
    response_json.pop("applicant")
    assert response.status_code == 200
    assert response_json == base_case


def test_update_case(client):
    updated_case = base_case.copy()
    updated_case["status"] = "In Progress"
    response = client.put("/api/cases/1", json=updated_case)
    response_json = generalize_json_data(response.json())
    assert response.status_code == 200
    assert response_json == updated_case


def test_update_case_invalid_id(client):
    response = client.put("/api/cases/-1", json=base_case)
    assert response.status_code == 404


def test_delete_case(client):
    response = client.delete("/api/cases/1")
    assert response.status_code == 204


def test_delete_case_invalid_id(client):
    response = client.delete("/api/cases/-1")
    assert response.status_code == 404
