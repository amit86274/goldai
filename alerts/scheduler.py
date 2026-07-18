
class AlertScheduler:
    def schedule(self, alert, run_at):
        return {"alert": alert, "run_at": run_at, "status": "scheduled"}
