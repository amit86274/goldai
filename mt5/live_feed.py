\
"""
Gold-AI
mt5/live_feed.py

Simple live MT5 market feed.
"""

from __future__ import annotations

import time
from typing import Callable, Optional

import MetaTrader5 as mt5


class LiveFeed:
    """Streams live ticks from MT5."""

    def __init__(
        self,
        symbol: str,
        poll_interval: float = 1.0,
    ):
        self.symbol = symbol
        self.poll_interval = poll_interval
        self.running = False
        self._last_tick_time = None

    def start(
        self,
        on_tick: Optional[Callable] = None,
    ) -> None:
        """Start polling live ticks."""
        if not mt5.initialize():
            raise RuntimeError(f"MT5 initialization failed: {mt5.last_error()}")

        self.running = True
        print(f"Listening for {self.symbol} ticks...")

        while self.running:
            tick = mt5.symbol_info_tick(self.symbol)

            if tick is not None:
                if tick.time != self._last_tick_time:
                    self._last_tick_time = tick.time

                    if on_tick:
                        on_tick(tick)
                    else:
                        print(
                            f"{tick.time} | "
                            f"Bid={tick.bid:.3f} "
                            f"Ask={tick.ask:.3f}"
                        )

            time.sleep(self.poll_interval)

    def stop(self):
        """Stop polling."""
        self.running = False
        mt5.shutdown()


def print_tick(tick):
    print(
        f"Time: {tick.time} "
        f"Bid: {tick.bid:.3f} "
        f"Ask: {tick.ask:.3f}"
    )


if __name__ == "__main__":
    feed = LiveFeed("XAUUSD", poll_interval=0.5)

    try:
        feed.start(print_tick)
    except KeyboardInterrupt:
        print("\nStopping...")
        feed.stop()
