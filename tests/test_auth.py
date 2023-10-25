import requests
from http import HTTPStatus


def test_auth(admin_auth):
    response = requests.post(
        url="https://restful-booker.herokuapp.com/auth",
        json={
            "username": admin_auth.username,
            "password": admin_auth.password}
    )
    # print(response.content)
    # print(response.json())
    assert HTTPStatus.OK == response.status_code
