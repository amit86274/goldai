
class SMSAlert:
    def send(self, phone, message):
        return {
            "channel":"sms",
            "phone":phone,
            "message":message,
            "status":"queued"
        }
