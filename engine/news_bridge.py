
class NewsBridge:
    def __init__(self, sentiment_engine):
        self.engine=sentiment_engine
    def sentiment(self,articles):
        return self.engine.analyze(articles)
