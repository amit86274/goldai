
class DatabaseConnection:
    def __init__(self, uri):
        self.uri = uri
        self.connected = False

    def connect(self):
        self.connected = True
        return self.connected

    def disconnect(self):
        self.connected = False
