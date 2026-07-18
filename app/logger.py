"""
Production Logger

app/logger.py
"""

from __future__ import annotations

import logging
import logging.handlers
import os
import sys
from pathlib import Path

LOG_DIRECTORY = Path("logs")
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "gold_ai.log"

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(threadName)s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class LoggerFactory:

    _configured = False

    @classmethod
    def build(cls) -> logging.Logger:

        logger = logging.getLogger("GoldAI")

        if cls._configured:
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            LOG_FORMAT,
            DATE_FORMAT
        )

        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)

        rotating = logging.handlers.RotatingFileHandler(
            filename=LOG_FILE,
            maxBytes=20 * 1024 * 1024,
            backupCount=20,
            encoding="utf8"
        )

        rotating.setFormatter(formatter)
        rotating.setLevel(logging.INFO)

        logger.addHandler(console)
        logger.addHandler(rotating)

        logger.propagate = False

        cls._configured = True

        return logger


logger = LoggerFactory.build()


def set_debug():

    logger.setLevel(logging.DEBUG)

    for handler in logger.handlers:
        handler.setLevel(logging.DEBUG)


def set_info():

    logger.setLevel(logging.INFO)

    for handler in logger.handlers:
        handler.setLevel(logging.INFO)


def set_warning():

    logger.setLevel(logging.WARNING)

    for handler in logger.handlers:
        handler.setLevel(logging.WARNING)


def set_error():

    logger.setLevel(logging.ERROR)

    for handler in logger.handlers:
        handler.setLevel(logging.ERROR)


def get_logger(name: str):

    return logger.getChild(name)