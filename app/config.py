from pydantic import BaseSettings
from pathlib import Path

ENV_PATH = Path(__file__).parent.parent / ".env"


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_port: int
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = str(ENV_PATH)


settings = Settings()
