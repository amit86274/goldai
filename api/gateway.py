
class APIGateway:
    def route(self, service, path):
        return {
            "service": service,
            "path": path,
            "status": "forwarded"
        }
