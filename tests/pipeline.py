class TestPipeline:
    def __init__(self):
        self.steps=[]
    def add_step(self,name):
        self.steps.append(name)
    def execute(self):
        return {'steps': self.steps, 'status':'success'}
