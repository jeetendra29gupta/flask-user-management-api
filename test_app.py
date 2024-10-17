import pytest
import requests


@pytest.fixture(scope="module")
def base_url():
    return "http://localhost:8181"


def test_get_all_users_no_users(base_url):
    url = f"{base_url}/users"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == []


def test_create_user_success(base_url):
    url = f"{base_url}/users"
    payload = {
        "username": "juju_raven_1814",
        "email": "jeetendra.gupta@gmail.com",
        "salary": 200,
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json().get("message") == "user created"


def test_create_user_missing_username(base_url):
    url = f"{base_url}/users"
    payload = {
        "email": "jeetendra.gupta@gmail.com",
        "salary": 200,
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 400
    assert response.json().get("message") == "Missing required parameters"


def test_create_user_missing_email(base_url):
    url = f"{base_url}/users"
    payload = {
        "username": "juju_raven_1814",
        "salary": 200,
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 400
    assert response.json().get("message") == "Missing required parameters"


def test_create_user_missing_salary(base_url):
    url = f"{base_url}/users"
    payload = {
        "email": "jeetendra.gupta@gmail.com",
        "salary": 200,
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 400
    assert response.json().get("message") == "Missing required parameters"


def test_get_all_users_success(base_url):
    url = f"{base_url}/users"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id_success(base_url):
    get_url = f"{base_url}/users/1"
    response = requests.get(get_url)
    assert response.status_code == 200
    assert response.json().get("username") == "juju_raven_1814"


def test_get_user_by_invalid_id(base_url):
    url = f"{base_url}/users/999"
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json().get("message") == "User not found"


def test_update_user_success(base_url):
    update_url = f"{base_url}/users/1"
    update_payload = {
        "username": "juju_raven_1814",
        "email": "jeetendra.gupta@gmail.com",
        "salary": 300,
    }
    response = requests.put(update_url, json=update_payload)
    assert response.status_code == 200
    assert response.json().get("message") == "User updated successfully"


def test_update_user_invalid_id(base_url):
    update_url = f"{base_url}/users/999"
    update_payload = {
        "username": "juju_raven_1814",
        "email": "jeetendra.gupta@gmail.com",
        "salary": 300,
    }
    response = requests.put(update_url, json=update_payload)
    assert response.status_code == 404
    assert response.json().get("message") == "User not found"


def test_partial_update_user_success(base_url):
    update_url = f"{base_url}/users/1"
    partial_payload = {"salary": 400, }
    response = requests.patch(update_url, json=partial_payload)
    assert response.status_code == 200
    assert response.json().get("message") == "User partially updated successfully"


def test_partial_update_user_invalid_id(base_url):
    update_url = f"{base_url}/users/999"
    partial_payload = {"salary": 400, }
    response = requests.patch(update_url, json=partial_payload)
    assert response.status_code == 404
    assert response.json().get("message") == "User not found"


def test_delete_user_success(base_url):
    delete_url = f"{base_url}/users/1"
    response = requests.delete(delete_url)
    assert response.status_code == 200
    assert response.json().get("message") == "User deleted successfully"


def test_delete_user_invalid_id(base_url):
    delete_url = f"{base_url}/users/999"
    response = requests.delete(delete_url)
    assert response.status_code == 404
    assert response.json().get("message") == "User not found"
