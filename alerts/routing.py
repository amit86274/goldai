
class AlertRouter:
    def route(self,priority):
        mapping={
            "LOW":["email"],
            "MEDIUM":["email","telegram"],
            "HIGH":["email","telegram","push","sms"]
        }
        return mapping.get(priority.upper(),["email"])
