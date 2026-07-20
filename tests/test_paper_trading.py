from strategy.paper_trading import PaperTradingEngine, TradeRecord


def test_paper_trading_engine_records_trade():
    engine = PaperTradingEngine(initial_balance=10000.0)
    record = engine.execute(action="BUY", confidence=0.9, position_size=100.0)

    assert isinstance(record, TradeRecord)
    assert record.action == "BUY"
    assert record.position_size == 100.0
    assert engine.balance > 0
