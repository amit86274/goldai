
class MultiAccountDashboard:
    def summary(self, accounts):
        return {
            "accounts": len(accounts),
            "total_balance": sum(a.get("balance", 0) for a in accounts),
            "total_equity": sum(a.get("equity", 0) for a in accounts)
        }
