"""Macro-economic scoring helpers."""
from __future__ import annotations

def inflation_signal(actual: float, forecast: float)->str:
    if actual>forecast:
        return "Higher Inflation"
    if actual<forecast:
        return "Lower Inflation"
    return "In Line"

def interest_rate_signal(current: float, previous: float)->str:
    if current>previous:
        return "Hawkish"
    if current<previous:
        return "Dovish"
    return "Unchanged"

def macro_score(signals:list[str])->int:
    score=0
    for s in signals:
        if s in ("Dovish","Lower Inflation"):
            score+=1
        elif s in ("Hawkish","Higher Inflation"):
            score-=1
    return score
