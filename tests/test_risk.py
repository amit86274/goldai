from strategy.risk_manager import position_size

def test_position():
    assert position_size(5000,2,100,1)==1
