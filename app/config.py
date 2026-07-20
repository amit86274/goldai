"""
app/config.py

Production Configuration Loader
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

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
    live_trading_enabled: bool

    mt5: MT5Config

    database: DatabaseConfig

    redis: RedisConfig

    ai: AIConfig

    def to_dict(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "live_trading_enabled": self.live_trading_enabled,
            "mt5": {
                "login": self.mt5.login,
                "server": self.mt5.server,
                "terminal_path": self.mt5.terminal_path,
                "timeout": self.mt5.timeout,
            },
            "database": {
                "host": self.database.host,
                "port": self.database.port,
                "database": self.database.database,
            },
            "redis": {
                "host": self.redis.host,
                "port": self.redis.port,
                "db": self.redis.db,
            },
            "ai": {
                "model_directory": self.ai.model_directory,
                "prediction_threshold": self.ai.prediction_threshold,
            },
        }


def _optional(name: str, default: str) -> str:

    value = os.getenv(name)

    if value is None or value == "":
        return default

    return value


settings = Settings(

    debug=os.getenv("DEBUG", "false").lower() == "true",

    live_trading_enabled=os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true",

    mt5=MT5Config(

        login=int(_optional("MT5_LOGIN", "0")),

        password=_optional("MT5_PASSWORD", ""),

        server=_optional("MT5_SERVER", "localhost"),

        terminal_path=_optional("MT5_TERMINAL", ""),

        timeout=int(_optional("MT5_TIMEOUT", "60000")),

    ),

    database=DatabaseConfig(

        host=_optional("POSTGRES_HOST", "localhost"),

        port=int(_optional("POSTGRES_PORT", "5432")),

        user=_optional("POSTGRES_USER", "postgres"),

        password=_optional("POSTGRES_PASSWORD", "postgres"),

        database=_optional("POSTGRES_DB", "gold_ai"),

    ),

    redis=RedisConfig(

        host=_optional("REDIS_HOST", "localhost"),

        port=int(_optional("REDIS_PORT", "6379")),

        db=int(_optional("REDIS_DB", "0")),

    ),

    ai=AIConfig(

        model_directory=_optional("MODEL_DIRECTORY", "models"),

        prediction_threshold=float(
            _optional(
                "PREDICTION_THRESHOLD",
                "0.75"
            )
        ),

    ),
)
