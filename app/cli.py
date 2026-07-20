from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from strategy.advanced_engine import AdvancedTradingEngine, MarketContext
from strategy.backtesting import BacktestEngine
from models.xgboost.mt5_pipeline import MT5XGBoostTrainer


def main() -> None:
    parser = argparse.ArgumentParser(description="Gold-AI CLI")
    parser.add_argument("--mode", choices=["signal", "backtest", "train-mt5"], default="signal")
    parser.add_argument("--symbol", default="XAUUSD")
    parser.add_argument("--probability", type=float, default=0.86)
    parser.add_argument("--trend", type=float, default=0.82)
    parser.add_argument("--volatility", type=float, default=0.18)
    parser.add_argument("--balance", type=float, default=10000.0)
    parser.add_argument("--risk", type=float, default=1.0)
    parser.add_argument("--max-position", type=float, default=0.02)
    parser.add_argument("--session", default="active")
    args = parser.parse_args()

    if args.mode == "train-mt5":
        import MetaTrader5 as mt5
        from app.config import settings
        from mt5.connector import ConnectionConfig, MT5Connector

        connector = MT5Connector(ConnectionConfig(login=settings.mt5.login, password=settings.mt5.password, server=settings.mt5.server, path=settings.mt5.terminal_path, timeout=settings.mt5.timeout))
        if not connector.connect():
            raise RuntimeError("unable to connect to MT5")
        try:
            mt5.symbol_select(args.symbol, True)
            # The terminal's currently confirmed history depth is 500 bars.
            daily = mt5.copy_rates_from_pos(args.symbol, mt5.TIMEFRAME_D1, 0, 500)
            weekly = mt5.copy_rates_from_pos(args.symbol, mt5.TIMEFRAME_W1, 0, 500)
            result = MT5XGBoostTrainer().train(daily, weekly, "data/model_artifacts/xauusd_d1_xgboost.joblib")
            print(json.dumps(asdict(result)))
        finally:
            connector.disconnect()
        return

    if args.mode == "signal":
        engine = AdvancedTradingEngine()
        context = MarketContext(
            probability=args.probability,
            trend_strength=args.trend,
            volatility=args.volatility,
            balance=args.balance,
            risk_percent=args.risk,
            max_position_size=args.max_position,
            market_session=args.session,
        )
        decision = engine.analyze(context)
        print(json.dumps({"action": decision.action, "confidence": decision.confidence, "position_size": decision.position_size, "reason": decision.reason}))
        return

    engine = BacktestEngine()
    result = engine.run(
        initial_balance=args.balance,
        trades=[(args.probability, args.trend, args.volatility, args.balance, args.risk, args.max_position, args.session)],
    )
    print(json.dumps({"final_balance": result.final_balance, "total_trades": result.total_trades, "pnl": result.pnl}))


if __name__ == "__main__":
    main()
