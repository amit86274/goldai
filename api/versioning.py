
class APIVersionManager:
    def __init__(self, version="v1"):
        self.version = version

    def route(self, path):
        return f"/api/{self.version}/{path.lstrip('/')}"
