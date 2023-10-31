import pytest
from pydantic_settings import BaseSettings, SettingsConfigDict
import requests
from http import HTTPStatus


class AdminAuth(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        env_prefix="QA_",
    )

    username: str
    password: str


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        env_prefix="QA_",
    )

    base_url: str


@pytest.fixture
def admin_auth() -> AdminAuth:
    return AdminAuth()


@pytest.fixture
def env_settings() -> EnvSettings:
    return EnvSettings()


@pytest.fixture
def admin_cookie(admin_auth, env_settings) -> dict:
    response = requests.post(
        url=f"{env_settings.base_url}auth",
        json=admin_auth.model_dump(),
    )
    if response.status_code == HTTPStatus.OK:
        return {"Cookie": f"token={response.json()['token']}"}
    else:
        raise RuntimeError("Auth token retrival error")
