
class MigrationManager:
    def __init__(self):
        self.migrations = []

    def add(self, migration):
        self.migrations.append(migration)

    def run(self):
        return len(self.migrations)
