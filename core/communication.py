
class MessageBus:
    def __init__(self):
        self.handlers={}
    def subscribe(self,topic,handler):
        self.handlers.setdefault(topic,[]).append(handler)
    def publish(self,topic,message):
        for h in self.handlers.get(topic,[]):
            h(message)
