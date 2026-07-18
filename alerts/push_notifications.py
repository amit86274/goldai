
class PushNotification:
    def send(self, device_id, title, message):
        return {
            "channel": "push",
            "device_id": device_id,
            "title": title,
            "message": message,
            "status": "queued"
        }
