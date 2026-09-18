from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str
    SECRET_KEY: str = Field(min_length=16)
    ALGORITHM: str

settings = Settings()