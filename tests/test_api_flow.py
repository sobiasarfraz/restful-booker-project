import logging
import requests

logger = logging.getLogger()

Base_url = "https://restful-booker.herokuapp.com"

def test_health():
    url = f"{Base_url}/ping"

    health = requests.get(url)

    logger.info(f"health check test, got the status code: {health.status_code}")
    assert health.status_code == 201, f"expected 201 but got {health.status_code}"

def test_get_all_booking():
    url = f"{Base_url}/booking"
    get_bookings = requests.get(url)
    logger.info(f"got all booking data, status code is {get_bookings.status_code}")
    assert get_bookings.status_code == 200, f"expected 200 but got {get_bookings.status_code}"
    all_booking = get_bookings.json()
    assert isinstance(all_booking, list), "expected list of bookings"
    logger.info("received list of all bookings")



def test_get_booking(create_booking):
    booking_id = create_booking["id"]
    original_data = create_booking["data"]
    url = f"{Base_url}/booking/{booking_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    logger.info(f"got booking with the id no: {booking_id}")
    assert data["firstname"] == original_data["firstname"], f"could not get the booking with id: {booking_id}, status code is: {response.status_code}"


def test_update_booking(auth_token, create_booking):
    booking_id = create_booking["id"]
    url = f"{Base_url}/booking/{booking_id}"
    updated_data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    response = requests.put(url, json=updated_data, headers=headers)
    response.raise_for_status()
    data = response.json()
    logger.info(f"update the booking")
    assert data["firstname"] == "James", f"data is not updated,got the {response.status_code} status code"


def test_parital_update(auth_token, create_booking):
    booking_id = create_booking["id"]
    url = f"{Base_url}/booking/{booking_id}"
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    data = {
        "firstname": "Sobia",
        "lastname": "Asif"
    }

    partial = requests.patch(url, headers=header, json=data)

    partial.raise_for_status()

    partial_data = partial.json()

    logger.info("patch test, just partially update the booking")
    assert partial_data["firstname"] == "Sobia", f"first name is still: {partial_data["firstname"]}, not updated "

def test_delete_booking(auth_token, create_booking):
    booking_id = create_booking["id"]
    url = f"{Base_url}/booking/{booking_id}"
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(url, headers=headers)
    logger.info("booking is deleted ")
    assert response.status_code == 201, f"expected status code is 201, but received: {response.status_code}"

