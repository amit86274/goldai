
import pytest

from strategy.advanced_engine import AdvancedTradingEngine, MarketContext

def test_engine_rejects_non_finite_market_data():
    context = MarketContext(float("nan"), 0.8, 0.1, 10_000.0, 1.0, 0.02, "active")

    with pytest.raises(ValueError, match="finite"):
        AdvancedTradingEngine().analyze(context)
