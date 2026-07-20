from strategy.advanced_engine import AdvancedTradingEngine, MarketContext, TradingDecision
from app.health import HealthMonitor


def test_engine_emits_buy_for_high_confidence_and_safe_risk():
    engine = AdvancedTradingEngine()
    context = MarketContext(
        probability=0.86,
        trend_strength=0.82,
        volatility=0.18,
        balance=10000.0,
        risk_percent=1.0,
        max_position_size=0.02,
        market_session="active",
    )

    decision = engine.analyze(context)

    assert decision.action == "BUY"
    assert decision.confidence >= 0.75
    assert decision.position_size > 0


def test_engine_waits_when_risk_is_too_high():
    engine = AdvancedTradingEngine()
    context = MarketContext(
        probability=0.84,
        trend_strength=0.75,
        volatility=0.35,
        balance=1000.0,
        risk_percent=5.0,
        max_position_size=0.01,
        market_session="active",
    )

    decision = engine.analyze(context)

    assert decision.action == "WAIT"
    assert decision.reason.lower().startswith("risk")


def test_health_monitor_tracks_state_changes():
    monitor = HealthMonitor()
    monitor.mark_running("engine ready")
    monitor.mark_warning("latency elevated")

    snapshot = monitor.snapshot()

    assert snapshot["status"] == "warning"
    assert snapshot["checks"][0]["name"] == "engine"
