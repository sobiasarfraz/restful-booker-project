import requests
import logging

logger = logging.getLogger()  ## python function

Base_url = "https://restful-booker.herokuapp.com"


def test_invalid_id():    #### negative case test for invalid id
    url = f"{Base_url}/booking/0000"    #### gave self created id
    response = requests.get(url)
    logger.info(f"testing with invalid id and status code is : {response.status_code}")
    assert response.status_code in [401, 403, 404]


def test_invalid_json_data(create_booking):   #### negative test case ... just pass wrong format of json data
    booking_id = create_booking["id"]
    url = f"{Base_url}/booking"
    header = {
        "Content-Type": "application/json"
    }

    data1 = '{"firstname": "Jim"'   ##### we gave wrong json format to test

    response = requests.post(url, data=data1, headers=header)
    logger.warning(f"testing with invalid json data, status code is: {response.status_code}")
    assert response.status_code in [400, 401, 403, 404, 500]


def test_invalid_token(create_booking):   #### negative case test ,,, invalid token
    booking_id = create_booking["id"]
    data = create_booking["data"]

    url = f"{Base_url}/booking/{booking_id}"

    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token=12345"

    }
    response = requests.put(url, json=data, headers=header)
    logger.warning(f"try to update data with invalid token, status: {response.status_code}")
    assert response.status_code in [401, 403, 404]



def test_delete_flow(auth_token):      #### error test just try to delete 2 times to check the flow
    url1 = f"{Base_url}/booking"
    data = {
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
    response = requests.post(url1, json=data)
    response.raise_for_status()
    id = response.json()["bookingid"]
    logger.info(f"create new data and got id: {id}, status is :{response.status_code}")

    header = {
        "Cookie": f"token={auth_token}"
    }

    ###  deleting the data
    response1 = requests.delete(url=f"{url1}/{id}", headers=header)
    logger.info(f"delete the data with the id: {id}, and status is: {response1.status_code}")
    assert  response1.status_code == 201

     ### deleting data again with same id
    response2 = requests.delete(url=f"{url1}/{id}", headers=header)
    logger.error(f"tried to delete again already deleted data, status is : {response2.status_code}")
    assert response2.status_code in [400, 401, 403, 404, 405]






