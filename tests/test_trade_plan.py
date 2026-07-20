import pytest

from strategy.trade_plan import TradePlanBuilder, TradePlanError, TradePlanRequest


def request(**overrides):
    values = {
        "action": "BUY",
        "confidence": 0.80,
        "entry_price": 2000.0,
        "atr": 10.0,
        "balance": 10_000.0,
        "risk_percent": 1.0,
        "value_per_price_unit": 100.0,
    }
    values.update(overrides)
    return TradePlanRequest(**values)


def test_trade_plan_calculates_atr_stop_target_and_risk_based_volume():
    plan = TradePlanBuilder().build(request())

    assert plan.stop_loss == 1985.0
    assert plan.take_profit == 2030.0
    assert plan.volume == 0.06
    assert plan.risk_amount == 100.0


def test_trade_plan_uses_sell_direction_for_protection_and_target():
    plan = TradePlanBuilder().build(request(action="SELL"))

    assert plan.stop_loss == 2015.0
    assert plan.take_profit == 1970.0


def test_trade_plan_refuses_low_confidence_entries():
    with pytest.raises(TradePlanError, match="confidence"):
        TradePlanBuilder().build(request(confidence=0.69))
