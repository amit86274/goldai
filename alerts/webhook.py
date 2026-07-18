
class WebhookAlert:
    def post(self, url, payload):
        return {
            "channel":"webhook",
            "url":url,
            "payload":payload,
            "status":"queued"
        }
