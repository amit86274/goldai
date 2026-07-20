from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass(slots=True)
class HealthCheck:
    name: str
    status: str
    message: str


class HealthMonitor:
    def __init__(self) -> None:
        self.checks: List[HealthCheck] = []

    def mark_running(self, message: str = "ok") -> None:
        self.checks.append(HealthCheck("engine", "ok", message))

    def mark_warning(self, message: str = "warning") -> None:
        self.checks.append(HealthCheck("engine", "warning", message))

    def mark_error(self, message: str = "error") -> None:
        self.checks.append(HealthCheck("engine", "error", message))

    def snapshot(self) -> Dict[str, Any]:
        if not self.checks:
            return {"status": "unknown", "checks": []}

        status = "ok"
        if any(check.status == "error" for check in self.checks):
            status = "error"
        elif any(check.status == "warning" for check in self.checks):
            status = "warning"

        return {"status": status, "checks": [{"name": check.name, "status": check.status, "message": check.message} for check in self.checks]}
