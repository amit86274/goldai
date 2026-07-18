
class QueryBuilder:
    def __init__(self):
        self.filters = {}

    def where(self, **kwargs):
        self.filters.update(kwargs)
        return self

    def build(self):
        return self.filters
