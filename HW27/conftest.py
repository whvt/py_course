import pytest
import requests


@pytest.fixture
def base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture
def auth_token(base_url):
    creds = {"username": "admin", "password": "password123"}
    response = requests.post(f"{base_url}/auth", json=creds)
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def created_booking(base_url, booking_data):
    response = requests.post(f"{base_url}/booking", json=booking_data)
    assert response.status_code == 200
    return response.json()["bookingid"]
