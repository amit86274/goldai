from __future__ import annotations

from typing import Callable, Dict, Any
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

from strategy.advanced_engine import AdvancedTradingEngine, MarketContext
from strategy.model_pipeline import ModelSignalPipeline
from strategy.trade_plan import TradePlanBuilder, TradePlanError, TradePlanRequest
from models.predictor import Predictor


class APIApplication:
    def __init__(self) -> None:
        self.routes: Dict[str, Callable[..., Any]] = {}

    def register(self, path: str, handler: Callable[..., Any]) -> None:
        self.routes[path] = handler


def create_app() -> Flask:
    app = Flask("gold-ai")
    CORS(app)
    engine = AdvancedTradingEngine()
    trade_plan_builder = TradePlanBuilder()
    model_path = Path("models/model_artifact.json")
    predictor = None

    if model_path.exists():
        predictor = Predictor(str(model_path))

    # A web worker must never establish a live trading session unless an
    # operator has explicitly opted in through configuration.
    from mt5.connector import MT5Connector, ConnectionConfig
    mt5_connector = None
    from app.config import settings

    if settings.live_trading_enabled:
        try:
            config = ConnectionConfig(
                login=settings.mt5.login,
                password=settings.mt5.password,
                server=settings.mt5.server,
                path=settings.mt5.terminal_path,
            )
            mt5_connector = MT5Connector(config)
            if not mt5_connector.connect():
                mt5_connector = None
        except Exception:
            app.logger.exception("MT5 connection failed")
            mt5_connector = None

    @app.get("/health")
    def health() -> Any:
        status = "ok" if not settings.live_trading_enabled or mt5_connector is not None else "warning"
        return jsonify({"service": "gold-ai", "status": status, "live_trading_enabled": settings.live_trading_enabled})

    @app.get("/price/<symbol>")
    def get_price(symbol: str) -> Any:
        """Get live price for a symbol from MT5"""
        if mt5_connector is None or not mt5_connector.is_connected():
            return jsonify({"error": "MT5 not connected"}), 503
        
        try:
            import MetaTrader5 as mt5
            tick = mt5.symbol_info_tick(symbol)
            if tick:
                return jsonify({"symbol": symbol, "price": tick.ask, "bid": tick.bid})
            else:
                return jsonify({"error": f"Symbol {symbol} not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @app.post("/decision")
    def decision() -> Any:
        payload = request.get_json(silent=True) or {}
        try:
            context = MarketContext(
                probability=float(payload.get("probability", 0.5)),
                trend_strength=float(payload.get("trend_strength", 0.5)),
                volatility=float(payload.get("volatility", 0.2)),
                balance=float(payload.get("balance", 10000.0)),
                risk_percent=float(payload.get("risk_percent", 1.0)),
                max_position_size=float(payload.get("max_position_size", 0.02)),
                market_session=str(payload.get("market_session", "active")),
            )
        except (TypeError, ValueError) as exc:
            return jsonify({"error": f"invalid decision input: {exc}"}), 400
        try:
            decision = engine.analyze(context)
        except ValueError as exc:
            return jsonify({"error": f"invalid decision input: {exc}"}), 400

        if predictor is not None:
            features = payload.get("features")
            if features is not None:
                signal = ModelSignalPipeline(predictor).generate_signal(features)
                if signal["action"] in {"BUY", "SELL"}:
                    decision = type(decision)(signal["action"], signal["confidence"], decision.position_size, signal["reason"])

        response = {"decision": {"action": decision.action, "confidence": decision.confidence, "position_size": decision.position_size, "reason": decision.reason}}
        if decision.action in {"BUY", "SELL"}:
            try:
                entry_price = payload.get("entry_price")
                if entry_price is None and mt5_connector is not None:
                    symbol = str(payload.get("symbol", ""))
                    tick = mt5_connector.tick(symbol) if symbol else None
                    entry_price = tick.ask if tick is not None and decision.action == "BUY" else tick.bid if tick is not None else None
                plan_request = TradePlanRequest(
                    action=decision.action,
                    confidence=decision.confidence,
                    entry_price=float(entry_price),
                    atr=float(payload["atr"]),
                    balance=context.balance,
                    risk_percent=context.risk_percent,
                    value_per_price_unit=float(payload["value_per_price_unit"]),
                    minimum_volume=float(payload.get("minimum_volume", 0.01)),
                    maximum_volume=float(payload.get("maximum_volume", 100.0)),
                    volume_step=float(payload.get("volume_step", 0.01)),
                    stop_atr_multiplier=float(payload.get("stop_atr_multiplier", 1.5)),
                    reward_to_risk=float(payload.get("reward_to_risk", 2.0)),
                    minimum_stop_distance=float(payload.get("minimum_stop_distance", 0.0)),
                )
                response["trade_plan"] = trade_plan_builder.build(plan_request).to_dict()
            except (KeyError, TypeError):
                response["trade_plan"] = None
                response["trade_plan_status"] = "entry_price (or a live symbol), atr, and value_per_price_unit are required"
            except (TypeError, ValueError, TradePlanError) as exc:
                response["trade_plan"] = None
                response["trade_plan_status"] = str(exc)

        return jsonify(response)

    return app
