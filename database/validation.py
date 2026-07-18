
class DataValidator:
    def validate(self, data, required):
        missing=[k for k in required if k not in data]
        return {"valid": len(missing)==0, "missing": missing}
