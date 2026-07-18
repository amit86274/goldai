"""
Gold-AI
mt5/symbols.py

Utilities for managing MT5 symbols and timeframes.
"""

from __future__ import annotations

from typing import List, Optional, Dict
import MetaTrader5 as mt5


TIMEFRAMES: Dict[str, int] = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15,
    "M30": mt5.TIMEFRAME_M30,
    "H1": mt5.TIMEFRAME_H1,
    "H4": mt5.TIMEFRAME_H4,
    "D1": mt5.TIMEFRAME_D1,
    "W1": mt5.TIMEFRAME_W1,
    "MN1": mt5.TIMEFRAME_MN1,
}


class SymbolManager:
    """Helper class for MT5 symbols."""

    @staticmethod
    def list_symbols() -> List[str]:
        symbols = mt5.symbols_get()
        return sorted([s.name for s in symbols]) if symbols else []

    @staticmethod
    def exists(symbol: str) -> bool:
        return mt5.symbol_info(symbol) is not None

    @staticmethod
    def enable(symbol: str) -> bool:
        if not SymbolManager.exists(symbol):
            return False
        info = mt5.symbol_info(symbol)
        if info.visible:
            return True
        return mt5.symbol_select(symbol, True)

    @staticmethod
    def disable(symbol: str) -> bool:
        if not SymbolManager.exists(symbol):
            return False
        return mt5.symbol_select(symbol, False)

    @staticmethod
    def info(symbol: str):
        return mt5.symbol_info(symbol)

    @staticmethod
    def tick(symbol: str):
        return mt5.symbol_info_tick(symbol)

    @staticmethod
    def supported_timeframes() -> Dict[str, int]:
        return TIMEFRAMES.copy()

    @staticmethod
    def timeframe(name: str) -> Optional[int]:
        return TIMEFRAMES.get(name.upper())


if __name__ == "__main__":
    print("Supported Timeframes:")
    for k in TIMEFRAMES:
        print(k)

    print("\nFirst 20 Symbols:")
    for s in SymbolManager.list_symbols()[:20]:
        print(s)
