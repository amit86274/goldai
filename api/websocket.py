
class WebSocketStream:
    def connect(self, client_id):
        return {"client": client_id, "status": "connected"}

    def publish(self, channel, payload):
        return {"channel": channel, "payload": payload}
