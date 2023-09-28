base_spacecraft = {
    "id": 0,
    "name": "test craft",
    "description": "test description",
    "affiliation": "test affiliation",
    "dimensions": "test dimensions",
    "appearances": 0,
}


def test_create_spacecraft(client):
    response = client.post("/api/spacecraft/", json=base_spacecraft)
    assert response.status_code == 201
    assert response.json() == base_spacecraft


def test_get_all_spacecraft(client):
    response = client.get("/api/spacecraft")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_spacecraft_paged(client):
    response = client.get("/api/spacecraft?page_number=0&page_size=10")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_spacecraft(client):
    response = client.get("/api/spacecraft/0")
    assert response.status_code == 200
    assert response.json() == base_spacecraft


def test_update_spacecraft(client):
    updated_spacecraft = base_spacecraft.copy()
    updated_spacecraft["appearances"] = 1

    response = client.put("/api/spacecraft/0", json=updated_spacecraft)
    assert response.status_code == 200
    assert response.json() == updated_spacecraft


def test_update_spacecraft_invalid_id(client):
    response = client.put("/api/spacecraft/-1", json=base_spacecraft)
    assert response.status_code == 404


def test_delete_spacecraft(client):
    response = client.delete("/api/spacecraft/0")
    assert response.status_code == 204


def test_delete_spacecraft_invalid_id(client):
    response = client.delete("/api/spacecraft/-1")
    assert response.status_code == 404
