from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class DevSettings(BaseSettings):
    #Redis
    REDIS_HOST: str
    REDIS_PASSWORD: str
    REDIS_PORT: str

    #Ebay
    EBAY_CLIENT: str
    EBAY_SECRET: str
    EBAY_BASE_URL: str

    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env", env_file_encoding="utf-8", extra="allow")

settings = DevSettings()
