"""Combine news items into one score."""
from __future__ import annotations
from .sentiment import score

def overall(news_items):
    if not news_items:
        return {"score":0,"label":"Neutral"}
    total=sum(score(item.get("title","")) for item in news_items)
    if total>0:
        label="Bullish"
    elif total<0:
        label="Bearish"
    else:
        label="Neutral"
    return {"score":total,"label":label}
