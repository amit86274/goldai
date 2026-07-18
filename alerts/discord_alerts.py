
class DiscordAlert:
    def send(self, webhook_url, message):
        return {
            "channel":"discord",
            "webhook":webhook_url,
            "message":message,
            "status":"queued"
        }
