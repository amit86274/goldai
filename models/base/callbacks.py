
class EarlyStopping:
    def __init__(self,rounds=50):
        self.rounds=rounds

class ModelCheckpoint:
    def __init__(self,path):
        self.path=path
