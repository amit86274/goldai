from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BacktestResult:
    initial_balance: float
    final_balance: float
    total_trades: int
    pnl: float


class BacktestEngine:
    def __init__(self) -> None:
        self._engine = None

    def run(self, initial_balance: float, trades) -> BacktestResult:
        balance = float(initial_balance)
        total_trades = 0

        for trade in trades:
            probability, trend_strength, volatility, balance_value, risk_percent, max_position_size, market_session = trade
            if market_session.lower() not in {"active", "open", "high_volatility"}:
                continue
            if volatility > 0.25:
                continue
            expected_return = (probability - 0.5) * 100.0 * (1.0 + trend_strength)
            balance += expected_return * (risk_percent / 100.0)
            total_trades += 1

        return BacktestResult(
            initial_balance=float(initial_balance),
            final_balance=balance,
            total_trades=total_trades,
            pnl=balance - float(initial_balance),
        )
