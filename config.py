import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    YANDEX_API_KEY: str
    YANDEX_API_SECRET: str

    VK_ACCESS_TOKEN: str
    VK_OWNER_ID: str

    CELERY_RESULT_BACKEND: str
    CELERY_BROKER_URL: str

    @property
    def DATABASE_URL(self):
        return (f"postgresql+asyncpg://"
                f"{self.POSTGRES_USER}:"
                f"{self.POSTGRES_PASSWORD}@"
                f"{self.POSTGRES_HOST}:"
                f"{self.POSTGRES_PORT}/"
                f"{self.POSTGRES_DB}")

    @property
    def VK_ACCESS_TOKEN_(self):
        return self.VK_ACCESS_TOKEN

    @property
    def VK_OWNER_ID_(self):
        return self.VK_OWNER_ID

    @property
    def CELERY_RESULT_BACKEND_(self):
        return self.CELERY_RESULT_BACKEND

    @property
    def CELERY_BROKER_URL_(self):
        return self.CELERY_BROKER_URL

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
