
class PositionSynchronizer:
    def sync(self, local_positions, broker_positions):
        broker={p["ticket"]:p for p in broker_positions}
        return {"missing":[p for p in local_positions if p["ticket"] not in broker]}
