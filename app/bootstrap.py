"""
app/bootstrap.py

Production Bootstrap
"""

from __future__ import annotations

import platform
import sys
from pathlib import Path

from app.config import settings
from app.logger import logger


class Bootstrap:

    def __init__(self):

        self.root = Path.cwd()

    def validate_environment(self):

        logger.info("Validating runtime environment...")

        self._check_python()

        self._check_directories()

        self._check_mt5()

        logger.info("Environment OK")

    def _check_python(self):

        if sys.version_info < (3, 12):
            raise RuntimeError(
                "Python 3.12+ required"
            )

    def _check_directories(self):

        required = [

            "logs",

            "models",

            "reports",

            "cache",

            "data",

            "backtests",

            "temp"

        ]

        for folder in required:

            path = self.root / folder

            path.mkdir(
                parents=True,
                exist_ok=True
            )

    def _check_mt5(self):

        terminal = Path(settings.mt5.terminal_path)

        if not terminal.exists():

            raise FileNotFoundError(

                f"MT5 terminal not found:\n{terminal}"

            )

    def system_information(self):

        logger.info("=" * 70)

        logger.info("Gold-AI Runtime")

        logger.info("=" * 70)

        logger.info("OS: %s", platform.system())

        logger.info("Release: %s", platform.release())

        logger.info("Python: %s", platform.python_version())

        logger.info("CPU: %s", platform.processor())

        logger.info("Root: %s", self.root)

        logger.info("=" * 70)


bootstrap = Bootstrap()