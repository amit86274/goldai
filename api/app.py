from __future__ import annotations

from typing import Callable, Dict, Any
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

from strategy.advanced_engine import AdvancedTradingEngine, MarketContext
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
    model_path = Path("models/model_artifact.json")
    predictor = None

    if model_path.exists():
        predictor = Predictor(str(model_path))

    # Import MT5 connector
    from mt5.connector import MT5Connector, ConnectionConfig
    mt5_connector = None
    
    try:
        from app.config import settings
        config = ConnectionConfig(
            login=settings.mt5.login,
            password=settings.mt5.password,
            server=settings.mt5.server,
            path=settings.mt5.terminal_path
        )
        mt5_connector = MT5Connector(config)
        if not mt5_connector.connect():
            mt5_connector = None
    except Exception as e:
        print(f"MT5 connection failed: {e}")
        mt5_connector = None

    @app.get("/health")
    def health() -> Any:
        return jsonify({"service": "gold-ai", "status": "ok"})

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
        context = MarketContext(
            probability=float(payload.get("probability", 0.5)),
            trend_strength=float(payload.get("trend_strength", 0.5)),
            volatility=float(payload.get("volatility", 0.2)),
            balance=float(payload.get("balance", 10000.0)),
            risk_percent=float(payload.get("risk_percent", 1.0)),
            max_position_size=float(payload.get("max_position_size", 0.02)),
            market_session=str(payload.get("market_session", "active")),
        )
        decision = engine.analyze(context)

        if predictor is not None:
            features = payload.get("features")
            if features is not None:
                probs = predictor.predict_proba([features])
                if probs is not None and len(probs[0]) > 1:
                    positive_prob = float(probs[0][1])
                    if positive_prob >= 0.7:
                        decision = type(decision)("BUY", positive_prob, decision.position_size, "model probability")
                    elif positive_prob <= 0.3:
                        decision = type(decision)("SELL", 1.0 - positive_prob, decision.position_size, "model probability")

        return jsonify({"decision": {"action": decision.action, "confidence": decision.confidence, "position_size": decision.position_size, "reason": decision.reason}})

    return app
