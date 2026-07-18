\
"""
Gold-AI
mt5/downloader.py

Download historical MT5 data and save it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import MetaTrader5 as mt5
import pandas as pd


class HistoryDownloader:
    """Download historical OHLC data from MT5."""

    def __init__(self, data_dir: str = "data/raw"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def download(
        self,
        symbol: str,
        timeframe: int,
        bars: int = 5000,
    ) -> pd.DataFrame:
        """Download the latest `bars` candles."""
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
        if rates is None:
            raise RuntimeError(f"Failed to download data: {mt5.last_error()}")

        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s")
        return df

    def save_csv(
        self,
        df: pd.DataFrame,
        symbol: str,
        timeframe_name: str,
    ) -> Path:
        """Save a dataframe to CSV."""
        filename = f"{symbol}_{timeframe_name}.csv"
        path = self.data_dir / filename
        df.to_csv(path, index=False)
        return path

    def save_sqlite(
        self,
        df: pd.DataFrame,
        database_path: str,
        table_name: str,
    ) -> None:
        """Save dataframe to SQLite."""
        import sqlite3

        conn = sqlite3.connect(database_path)
        try:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
        finally:
            conn.close()

    def update(
        self,
        symbol: str,
        timeframe: int,
        timeframe_name: str,
        bars: int = 500,
        database_path: Optional[str] = None,
    ) -> pd.DataFrame:
        """Download and optionally persist the latest data."""
        df = self.download(symbol, timeframe, bars)
        self.save_csv(df, symbol, timeframe_name)

        if database_path:
            table = f"{symbol}_{timeframe_name}"
            self.save_sqlite(df, database_path, table)

        return df


if __name__ == "__main__":
    if not mt5.initialize():
        raise SystemExit(f"MT5 initialize failed: {mt5.last_error()}")

    downloader = HistoryDownloader()

    df = downloader.update(
        symbol="XAUUSD",
        timeframe=mt5.TIMEFRAME_H1,
        timeframe_name="H1",
        bars=1000,
    )

    print(df.tail())

    mt5.shutdown()
