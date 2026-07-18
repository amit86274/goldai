"""
Gold-AI
mt5/connector.py

Production-ready MT5 connector (Version 1)
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Optional, Any

try:
    import MetaTrader5 as mt5
except ImportError as exc:
    raise ImportError(
        "MetaTrader5 package is not installed. "
        "Install with: pip install MetaTrader5"
    ) from exc


@dataclass
class ConnectionConfig:
    login: Optional[int] = None
    password: Optional[str] = None
    server: Optional[str] = None
    path: Optional[str] = None
    timeout: int = 60000
    portable: bool = False


class MT5Connector:
    """MetaTrader 5 connection manager."""

    def __init__(self, config: ConnectionConfig):
        self.config = config
        self.logger = logging.getLogger("GoldAI.MT5")
        if not self.logger.handlers:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s | %(levelname)s | %(message)s"
            )
        self.connected = False

    def connect(self) -> bool:
        """Initialize and connect to MT5."""
        self.logger.info("Initializing MT5...")
        ok = mt5.initialize(
            path=self.config.path,
            login=self.config.login,
            password=self.config.password,
            server=self.config.server,
            timeout=self.config.timeout,
            portable=self.config.portable,
        )
        self.connected = bool(ok)
        if self.connected:
            self.logger.info("Connected successfully.")
        else:
            self.logger.error("Connection failed: %s", mt5.last_error())
        return self.connected

    def disconnect(self) -> None:
        """Shutdown MT5."""
        mt5.shutdown()
        self.connected = False
        self.logger.info("Disconnected.")

    def reconnect(self, retries: int = 3, delay: int = 5) -> bool:
        """Reconnect to MT5."""
        self.disconnect()
        for i in range(retries):
            self.logger.info("Reconnect attempt %d/%d", i + 1, retries)
            if self.connect():
                return True
            time.sleep(delay)
        return False

    def is_connected(self) -> bool:
        return self.connected

    def account_info(self) -> Optional[Any]:
        if not self.connected:
            return None
        return mt5.account_info()

    def terminal_info(self) -> Optional[Any]:
        if not self.connected:
            return None
        return mt5.terminal_info()

    def version(self):
        return mt5.version()

    def last_error(self):
        return mt5.last_error()


if __name__ == "__main__":
    # Fill these values or load from your config later.
    cfg = ConnectionConfig(
        login=None,
        password=None,
        server=None,
        path=None,
    )

    connector = MT5Connector(cfg)

    if connector.connect():
        print("Connected")
        print("Version:", connector.version())
        print("Terminal:", connector.terminal_info())
        print("Account:", connector.account_info())
        connector.disconnect()
    else:
        print("Failed:", connector.last_error())
