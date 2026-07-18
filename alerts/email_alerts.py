
class EmailAlert:
    def __init__(self, sender=None):
        self.sender = sender

    def send(self, recipient, subject, message):
        return {
            "channel": "email",
            "recipient": recipient,
            "subject": subject,
            "message": message,
            "status": "queued"
        }
