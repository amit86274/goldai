"""Risk-controlled conversion of a trading signal into an executable trade plan."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import floor, isfinite
from typing import Literal


Side = Literal["BUY", "SELL"]


@dataclass(frozen=True, slots=True)
class TradePlanRequest:
    action: Side
    confidence: float
    entry_price: float
    atr: float
    balance: float
    risk_percent: float
    value_per_price_unit: float
    minimum_volume: float = 0.01
    maximum_volume: float = 100.0
    volume_step: float = 0.01
    stop_atr_multiplier: float = 1.5
    reward_to_risk: float = 2.0
    minimum_stop_distance: float = 0.0


@dataclass(frozen=True, slots=True)
class TradePlan:
    action: Side
    confidence: float
    entry_price: float
    stop_loss: float
    take_profit: float
    volume: float
    risk_amount: float
    stop_distance: float
    reward_to_risk: float
    reason: str

    def to_dict(self) -> dict[str, float | str]:
        return asdict(self)


class TradePlanError(ValueError):
    """Raised when a plan cannot be safely calculated from the supplied data."""


class TradePlanBuilder:
    """Build trade plans using ATR stops and fixed-fractional risk sizing."""

    def __init__(self, minimum_confidence: float = 0.70) -> None:
        if not 0.0 <= minimum_confidence <= 1.0:
            raise ValueError("minimum_confidence must be between 0 and 1")
        self.minimum_confidence = minimum_confidence

    def build(self, request: TradePlanRequest) -> TradePlan:
        self._validate(request)
        if request.confidence < self.minimum_confidence:
            raise TradePlanError("confidence is below the entry threshold")

        stop_distance = max(
            request.atr * request.stop_atr_multiplier,
            request.minimum_stop_distance,
        )
        risk_amount = request.balance * request.risk_percent / 100.0
        raw_volume = risk_amount / (stop_distance * request.value_per_price_unit)
        volume = self._normalise_volume(raw_volume, request)
        if volume < request.minimum_volume:
            raise TradePlanError("risk budget is too small for the broker minimum volume")

        if request.action == "BUY":
            stop_loss = request.entry_price - stop_distance
            take_profit = request.entry_price + stop_distance * request.reward_to_risk
        else:
            stop_loss = request.entry_price + stop_distance
            take_profit = request.entry_price - stop_distance * request.reward_to_risk

        return TradePlan(
            action=request.action,
            confidence=request.confidence,
            entry_price=request.entry_price,
            stop_loss=stop_loss,
            take_profit=take_profit,
            volume=volume,
            risk_amount=risk_amount,
            stop_distance=stop_distance,
            reward_to_risk=request.reward_to_risk,
            reason="ATR stop and fixed-fractional risk sizing",
        )

    @staticmethod
    def _normalise_volume(raw_volume: float, request: TradePlanRequest) -> float:
        capped_volume = min(raw_volume, request.maximum_volume)
        return floor(capped_volume / request.volume_step) * request.volume_step

    @staticmethod
    def _validate(request: TradePlanRequest) -> None:
        if request.action not in {"BUY", "SELL"}:
            raise TradePlanError("action must be BUY or SELL")
        numeric_values = {
            "confidence": request.confidence,
            "entry_price": request.entry_price,
            "atr": request.atr,
            "balance": request.balance,
            "risk_percent": request.risk_percent,
            "value_per_price_unit": request.value_per_price_unit,
            "minimum_volume": request.minimum_volume,
            "maximum_volume": request.maximum_volume,
            "volume_step": request.volume_step,
            "stop_atr_multiplier": request.stop_atr_multiplier,
            "reward_to_risk": request.reward_to_risk,
            "minimum_stop_distance": request.minimum_stop_distance,
        }
        if not all(isfinite(value) for value in numeric_values.values()):
            raise TradePlanError("all trade-plan values must be finite")
        if not 0.0 <= request.confidence <= 1.0:
            raise TradePlanError("confidence must be between 0 and 1")
        if request.entry_price <= 0 or request.atr <= 0 or request.balance <= 0:
            raise TradePlanError("entry_price, atr, and balance must be positive")
        if not 0 < request.risk_percent <= 100:
            raise TradePlanError("risk_percent must be between 0 and 100")
        if request.value_per_price_unit <= 0 or request.volume_step <= 0:
            raise TradePlanError("value_per_price_unit and volume_step must be positive")
        if not 0 < request.minimum_volume <= request.maximum_volume:
            raise TradePlanError("volume bounds are invalid")
        if request.stop_atr_multiplier <= 0 or request.reward_to_risk <= 0:
            raise TradePlanError("stop and reward multipliers must be positive")
        if request.minimum_stop_distance < 0:
            raise TradePlanError("minimum_stop_distance cannot be negative")
