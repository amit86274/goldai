from strategy.backtesting import BacktestEngine, BacktestResult


def test_backtest_engine_generates_result():
    engine = BacktestEngine()
    result = engine.run(
        initial_balance=10000.0,
        trades=[(0.86, 0.82, 0.18, 10000.0, 1.0, 0.02, "active")],
    )

    assert isinstance(result, BacktestResult)
    assert result.final_balance > 0
    assert result.total_trades == 1
