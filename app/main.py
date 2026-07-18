"""
Gold-AI
Application Entry Point

Production Bootstrap
"""

from __future__ import annotations

import signal
import sys
import traceback
from pathlib import Path

from app.logger import logger

from app.bootstrap import bootstrap

from app.banner import show

class GoldAIApplication:
    """
    Main application bootstrap.
    """

    def __init__(self) -> None:
        self.running = False

    def initialize(self) -> None:
        logger.info("=" * 80)
        logger.info("Starting Gold-AI")
        logger.info("=" * 80)

        self._create_runtime_directories()

        logger.info("Bootstrap complete")

    def _create_runtime_directories(self) -> None:
        directories = [
            "logs",
            "data",
            "cache",
            "models",
            "reports",
            "backtests",
            "temp",
        ]

        for directory in directories:
            Path(directory).mkdir(exist_ok=True)

    def run(self) -> None:
        self.running = True

        logger.info("Gold-AI Engine Running")

        while self.running:
            signal.pause()

    def shutdown(self) -> None:
        logger.info("Shutdown requested")
        self.running = False
        logger.info("Gold-AI stopped")


app = GoldAIApplication()


def signal_handler(signum, frame):
    logger.info(f"Signal received: {signum}")
    app.shutdown()
    sys.exit(0)


def main():

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:

      show()
      bootstrap.validate_environment()

      bootstrap.system_information()

      app.initialize()

      app.run()

    except KeyboardInterrupt:

        app.shutdown()

    except Exception:

        logger.exception(traceback.format_exc())

        app.shutdown()

        raise


if __name__ == "__main__":
    main()