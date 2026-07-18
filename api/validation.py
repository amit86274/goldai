
class RequestValidator:
    def require(self, payload, fields):
        missing=[f for f in fields if f not in payload]
        return {"valid": len(missing)==0, "missing": missing}
