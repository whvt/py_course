from datetime import datetime, timedelta


# Generate booking dates
def generate_booking_dates():
    checkin = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
    checkout = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    return {"checkin": checkin, "checkout": checkout}


booking_data = {
    "firstname": "Nikita",
    "lastname": "Test",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": generate_booking_dates(),
    "additionalneeds": "Breakfast",
}

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
    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"],
}
