import pytest
import jsonschema
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
def created_booking(base_url):
    booking_data = {
        "firstname": "Nikita",
        "lastname": "Test",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-05-10", "checkout": "2025-05-15"},
        "additionalneeds": "Breakfast",
    }
    response = requests.post(f"{base_url}/booking", json=booking_data)
    assert response.status_code == 200
    return response.json()["bookingid"], booking_data


def test_get_booking(base_url, created_booking):
    booking_id = created_booking[0]
    response = requests.get(f"{base_url}/booking/{booking_id}")
    assert response.status_code == 200


def test_update_booking(base_url, auth_token, created_booking):
    booking_id = created_booking[0]
    updated_data = {
        "firstname": "Nikita",
        "lastname": "Updated",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {"checkin": "2025-06-01", "checkout": "2025-06-10"},
        "additionalneeds": "Lunch",
    }
    headers = {"Content-Type": "application/json", "Cookie": f"token={auth_token}"}
    response = requests.put(
        f"{base_url}/booking/{booking_id}", json=updated_data, headers=headers
    )
    assert response.status_code == 200


def test_partial_update_booking(base_url, auth_token, created_booking):
    partial_data = {"totalprice": 250}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}",
    }
    response = requests.patch(
        f"{base_url}/booking/{created_booking}", json=partial_data, headers=headers
    )
    assert response.status_code == 405


def test_filter_bookings(base_url):
    response = requests.get(f"{base_url}/booking?firstname=Nikita&lastname=Test")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_booking(base_url, auth_token, created_booking):
    booking_id = created_booking[0]
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f"{base_url}/booking/{booking_id}", headers=headers)
    assert response.status_code == 201


def test_validate_booking_json_schema(base_url, created_booking):
    booking_id, _ = created_booking
    response = requests.get(f"{base_url}/booking/{booking_id}")
    assert response.status_code == 200

    expected_schema = {
        "type": "object",
        "properties": {
            "firstname": {"type": "string"},
            "lastname": {"type": "string"},
            "totalprice": {"type": "integer"},
            "depositpaid": {"type": "boolean"},
            "bookingdates": {
                "type": "object",
                "properties": {
                    "checkin": {"type": "string"},
                    "checkout": {"type": "string"},
                },
                "required": ["checkin", "checkout"],
            },
            "additionalneeds": {"type": "string"},
        },
        "required": [
            "firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates",
        ],
    }

    jsonschema.validate(instance=response.json(), schema=expected_schema)


def test_get_invalid_booking(base_url):
    invalid_booking_id = 999999
    response = requests.get(f"{base_url}/booking/{invalid_booking_id}")
    assert response.status_code == 404


def test_update_booking_without_auth(base_url, created_booking):
    booking_id = created_booking[0]
    updated_data = {"firstname": "Invalid Update"}
    headers = {"Content-Type": "application/json"}  # Missing token
    response = requests.put(
        f"{base_url}/booking/{booking_id}", json=updated_data, headers=headers
    )
    assert response.status_code == 403


def test_create_booking_missing_fields(base_url):
    incomplete_data = {
        "firstname": "John",
        "lastname": "Doe",
        # Missing totalprice, depositpaid, bookingdates
    }
    response = requests.post(f"{base_url}/booking", json=incomplete_data)
    assert response.status_code in [400, 500]
