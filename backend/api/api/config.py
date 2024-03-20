from pathlib import Path

from pydantic_settings import BaseSettings

file_dir = Path(__file__).resolve().parent


class Settings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool = True

    class Config:
        env_file = f"{file_dir}/.env"


config = Settings()
