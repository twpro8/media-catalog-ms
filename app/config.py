"""
Config module.
"""

from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Base settings class.
    """

    MODE: Literal["TEST", "LOCAL", "DEV", "PROD"]
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARN", "ERROR"]

    APP_NAME: str = "Rest API"
    APP_VERSION: str = "0.1.0"

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def DB_URL(self):  # noqa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
