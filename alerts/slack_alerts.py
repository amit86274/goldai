
class SlackAlert:
    def send(self, webhook_url, message):
        return {
            "channel":"slack",
            "webhook":webhook_url,
            "message":message,
            "status":"queued"
        }
