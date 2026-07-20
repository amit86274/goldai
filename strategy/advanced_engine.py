from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class MarketContext:
    probability: float
    trend_strength: float
    volatility: float
    balance: float
    risk_percent: float
    max_position_size: float
    market_session: str


@dataclass(slots=True)
class TradingDecision:
    action: str
    confidence: float
    position_size: float
    reason: str


class AdvancedTradingEngine:
    def __init__(self, min_confidence: float = 0.72, max_volatility: float = 0.25) -> None:
        self.min_confidence = min_confidence
        self.max_volatility = max_volatility

    def analyze(self, context: MarketContext) -> TradingDecision:
        if context.market_session.lower() not in {"active", "open", "high_volatility"}:
            return TradingDecision("WAIT", 0.0, 0.0, "market session is closed")

        if context.volatility > self.max_volatility:
            return TradingDecision("WAIT", 0.0, 0.0, "risk: volatility too high")

        risk_budget = context.balance * (context.risk_percent / 100.0)
        position_size = min(risk_budget, context.balance * context.max_position_size)

        if position_size <= 0:
            return TradingDecision("WAIT", 0.0, 0.0, "risk: position size below threshold")

        confidence = min(0.99, 0.5 + (context.probability - 0.5) * 0.8 + context.trend_strength * 0.2)

        if confidence < self.min_confidence:
            return TradingDecision("WAIT", confidence, 0.0, "confidence below threshold")

        if context.probability >= 0.55:
            return TradingDecision("BUY", confidence, position_size, "high probability bullish setup")

        return TradingDecision("SELL", confidence, position_size, "high probability bearish setup")
