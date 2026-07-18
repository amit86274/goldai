
class NewsRepository:
    def save(self, article):
        return {"status": "saved", "article": article}
