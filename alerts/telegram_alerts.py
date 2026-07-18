
class TelegramAlert:
    def send(self, chat_id, message):
        return {
            "channel": "telegram",
            "chat_id": chat_id,
            "message": message,
            "status": "queued"
        }
