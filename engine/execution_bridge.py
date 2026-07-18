
class ExecutionBridge:
    def execute(self,executor,decision):
        if decision=="NO_TRADE":
            return {"status":"skipped"}
        return executor.execute(decision)
