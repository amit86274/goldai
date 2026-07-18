"""
app/config.py

Production Configuration Loader
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT_DIR / ".env"

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)


@dataclass(slots=True)
class MT5Config:
    login: int
    password: str
    server: str
    terminal_path: str
    timeout: int = 60000


@dataclass(slots=True)
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str


@dataclass(slots=True)
class RedisConfig:
    host: str
    port: int
    db: int


@dataclass(slots=True)
class AIConfig:
    model_directory: str
    prediction_threshold: float


@dataclass(slots=True)
class Settings:

    debug: bool

    mt5: MT5Config

    database: DatabaseConfig

    redis: RedisConfig

    ai: AIConfig


def _required(name: str) -> str:

    value = os.getenv(name)

    if value is None or value == "":
        raise RuntimeError(f"Environment variable '{name}' is missing")

    return value


settings = Settings(

    debug=os.getenv("DEBUG", "false").lower() == "true",

    mt5=MT5Config(

        login=int(_required("MT5_LOGIN")),

        password=_required("MT5_PASSWORD"),

        server=_required("MT5_SERVER"),

        terminal_path=_required("MT5_TERMINAL"),

    ),

    database=DatabaseConfig(

        host=_required("POSTGRES_HOST"),

        port=int(_required("POSTGRES_PORT")),

        user=_required("POSTGRES_USER"),

        password=_required("POSTGRES_PASSWORD"),

        database=_required("POSTGRES_DB"),

    ),

    redis=RedisConfig(

        host=_required("REDIS_HOST"),

        port=int(_required("REDIS_PORT")),

        db=int(os.getenv("REDIS_DB", "0")),

    ),

    ai=AIConfig(

        model_directory=os.getenv("MODEL_DIRECTORY", "models"),

        prediction_threshold=float(
            os.getenv(
                "PREDICTION_THRESHOLD",
                "0.75"
            )
        ),

    ),
)