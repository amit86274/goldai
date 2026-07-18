
class BackupManager:
    def backup(self, destination):
        return {"status": "success", "destination": destination}

    def restore(self, source):
        return {"status": "restored", "source": source}
