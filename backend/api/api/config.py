import logging
from datetime import datetime
from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings
from pythonjsonlogger import jsonlogger


class Settings(BaseSettings):
    SECRET_KEY: str
    ALLOWED_HOSTS: List[str]
    DEBUG: bool = True

    class Config:
        __file_dir = Path(__file__).resolve().parent
        env_file = f"{__file_dir}/.env"


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)

        if not log_record.get("timestamp"):
            log_record["timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


config = Settings()
logger = logging.getLogger("main")
