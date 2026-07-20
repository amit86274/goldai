from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import List, Dict, Any


@dataclass(slots=True)
class TradeRecord:
    action: str
    confidence: float
    position_size: float
    balance_after: float
    note: str


class PaperTradingEngine:
    def __init__(self, initial_balance: float = 10000.0, journal_path: str | None = None) -> None:
        self.balance = float(initial_balance)
        self.journal_path = Path(journal_path or "data/paper_trading_journal.json")
        self.journal_path.parent.mkdir(parents=True, exist_ok=True)
        self.records: List[TradeRecord] = []

    def execute(self, action: str, confidence: float, position_size: float, note: str = "paper trade") -> TradeRecord:
        if action not in {"BUY", "SELL", "WAIT"}:
            raise ValueError("action must be BUY, SELL, or WAIT")

        if action == "WAIT":
            record = TradeRecord(action=action, confidence=confidence, position_size=0.0, balance_after=self.balance, note=note)
        else:
            self.balance = max(0.0, self.balance - position_size)
            record = TradeRecord(action=action, confidence=confidence, position_size=position_size, balance_after=self.balance, note=note)

        self.records.append(record)
        self._persist()
        return record

    def _persist(self) -> None:
        payload = {
            "balance": self.balance,
            "records": [asdict(record) for record in self.records],
        }
        self.journal_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load(self) -> Dict[str, Any]:
        if not self.journal_path.exists():
            return {"balance": self.balance, "records": []}
        return json.loads(self.journal_path.read_text(encoding="utf-8"))
