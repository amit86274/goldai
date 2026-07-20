"""
Gold-AI
Application Entry Point

Production Bootstrap
"""

from __future__ import annotations

import signal
import sys
import time
import traceback
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.logger import logger
from app.bootstrap import bootstrap
from app.banner import show
from app.health import HealthMonitor
from app.config import settings
from strategy.advanced_engine import AdvancedTradingEngine, MarketContext
from strategy.paper_trading import PaperTradingEngine
from strategy.model_pipeline import ModelSignalPipeline
from models.xgboost.model import XGBoostModel
from mt5.connector import ConnectionConfig, MT5Connector

class GoldAIApplication:
    """
    Main application bootstrap.
    """

    def __init__(self) -> None:
        self.running = False
        self.health_monitor = HealthMonitor()
        self.engine = AdvancedTradingEngine()
        self.paper_engine = PaperTradingEngine(initial_balance=10000.0)
        self.model_pipeline = None
        self.mt5_connector = None

    def initialize(self) -> None:
        logger.info("=" * 80)
        logger.info("Starting Gold-AI")
        logger.info("=" * 80)

        self._create_runtime_directories()
        self._initialize_mt5()
        self._initialize_model_pipeline()
        self.health_monitor.mark_running("core modules initialized")

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

    def _initialize_mt5(self) -> None:
        try:
            config = ConnectionConfig(
                login=None,
                password=None,
                server=None,
                path=None,
                timeout=60000,
            )
            self.mt5_connector = MT5Connector(config)
            if self.mt5_connector.connect():
                logger.info("MT5 connected")
                self.health_monitor.mark_running("MT5 connected")
            else:
                logger.warning("MT5 unavailable; continuing in offline mode")
                self.health_monitor.mark_warning("MT5 unavailable")
        except Exception as exc:
            logger.warning("MT5 initialization failed: %s", exc)
            self.health_monitor.mark_warning("MT5 unavailable")

    def _initialize_model_pipeline(self) -> None:
        try:
            model = XGBoostModel()
            sample_features = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]]
            sample_labels = [1]
            model.train(sample_features, sample_labels)
            self.model_pipeline = ModelSignalPipeline(model=model)
            logger.info("Model pipeline initialized")
            self.health_monitor.mark_running("model pipeline ready")
        except Exception as exc:
            logger.warning("Model pipeline initialization failed: %s", exc)
            self.model_pipeline = None
            self.health_monitor.mark_warning("model pipeline unavailable")

    def run(self) -> None:
        self.running = True

        logger.info("Gold-AI Engine Running")

        sample_context = MarketContext(
            probability=0.86,
            trend_strength=0.82,
            volatility=0.18,
            balance=10000.0,
            risk_percent=1.0,
            max_position_size=0.02,
            market_session="active",
        )

        if self.model_pipeline is not None:
            model_signal = self.model_pipeline.generate_signal([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
            logger.info("Model signal: %s | confidence=%.2f", model_signal["action"], model_signal["confidence"])
            decision = self.engine.analyze(sample_context)
            if model_signal["action"] in {"BUY", "SELL"}:
                decision = type(decision)(model_signal["action"], model_signal["confidence"], decision.position_size, model_signal["reason"])
        else:
            decision = self.engine.analyze(sample_context)

        self.paper_engine.execute(action=decision.action, confidence=decision.confidence, position_size=decision.position_size, note="sample decision")
        logger.info("Sample decision: %s | confidence=%.2f | size=%.2f", decision.action, decision.confidence, decision.position_size)

        while self.running:
            time.sleep(1)

    def shutdown(self) -> None:
        logger.info("Shutdown requested")
        self.running = False
        self.health_monitor.mark_warning("service shutting down")
        logger.info("Gold-AI stopped")

    def runtime_status(self) -> dict:
        return {
            "running": self.running,
            "mt5_connected": self.mt5_connector is not None and self.mt5_connector.is_connected(),
            "health": self.health_monitor.snapshot(),
            "config": settings.to_dict(),
            "paper_trading_balance": self.paper_engine.balance,
            "paper_trading_records": len(self.paper_engine.records),
            "model_pipeline_ready": self.model_pipeline is not None,
        }


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

    except Exception as exc:
        logger.exception("Gold-AI startup failed: %s", exc)
        app.shutdown()
        raise


if __name__ == "__main__":
    main()