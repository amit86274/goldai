
class TransactionManager:
    def begin(self):
        return "BEGIN"

    def commit(self):
        return "COMMIT"

    def rollback(self):
        return "ROLLBACK"
