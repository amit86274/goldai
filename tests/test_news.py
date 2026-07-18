
from news.sentiment import label

def test_sentiment():
    assert label("gold bullish")=="Bullish"
