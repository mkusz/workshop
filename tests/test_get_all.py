import pytest
import requests


@pytest.mark.smoke
@pytest.mark.wip
def test_get_all(admin_cookie, env_settings):
    response = requests.get(
        url=f"{env_settings.base_url}booking",
        cookies=admin_cookie,
    )
    assert len(response.json()) >= 1
