
class ORMModel:
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def to_dict(self):
        return self.__dict__
