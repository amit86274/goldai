
class NotificationAnalytics:
    def summary(self, sent, failed):
        total=sent+failed
        return {"sent":sent,"failed":failed,
                "success_rate": sent/total if total else 0.0}
