
class LiveDashboard:
    def snapshot(self,equity,balance,positions):
        return {"equity":equity,"balance":balance,"open_positions":len(positions)}
