
def allow_news_trade(impact,minutes_before=30):
    blocked={"HIGH"}
    return impact.upper() not in blocked
