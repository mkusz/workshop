import requests
from http import HTTPStatus


def test_auth(admin_auth, env_settings):
    response = requests.post(
        url=f"{env_settings.base_url}auth",
        json={
            "username": admin_auth.username,
            "password": admin_auth.password}
    )
    assert HTTPStatus.OK == response.status_code
    assert "token" in response.json()
