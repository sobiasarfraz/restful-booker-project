import pytest
import requests
import logging
from logs_setup import setup_logging

Base_url = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="module")
def auth_token():
    url = f"{Base_url}/auth"
    credentials = {"username": "admin", "password": "password123"}
    response = requests.post(url, json=credentials)
    response.raise_for_status()
    token = response.json()["token"]
    return token

@pytest.fixture(scope="module")
def create_booking():
    url = f"{Base_url}/booking"
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, json=booking_data)
    response.raise_for_status()
    booking_id = response.json()["bookingid"]
    return {"id": booking_id, "data": booking_data}  # return dict instead of tuple ## retuning booking id and booking data to use


setup_logging()