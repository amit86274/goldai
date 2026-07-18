def trading_hours(hour:int)->bool:
    return 7 <= hour <= 21

def news_filter(impact:str)->bool:
    return impact.lower() != "high"
