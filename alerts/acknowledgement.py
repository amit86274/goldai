
class AlertAcknowledgement:
    def acknowledge(self, alert_id, user):
        return {"alert_id": alert_id, "user": user, "acknowledged": True}
