import requests


def create_booking(base_url, booking_data):
    response = requests.post(f"{base_url}/booking", json=booking_data)
    assert response.status_code == 200
    return response.json()["bookingid"]


def update_booking(base_url, booking_id, auth_token, updated_data):
    headers = {"Content-Type": "application/json", "Cookie": f"token={auth_token}"}
    response = requests.put(
        f"{base_url}/booking/{booking_id}", json=updated_data, headers=headers
    )
    return response


def delete_booking(base_url, booking_id, auth_token):
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f"{base_url}/booking/{booking_id}", headers=headers)
    return response
