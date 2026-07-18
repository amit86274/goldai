from strategy.portfolio import Portfolio
def test_deposit():
    p=Portfolio(); p.deposit(100)
    assert p.balance==100
