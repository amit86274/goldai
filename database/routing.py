
class ReadWriteRouter:
    def route(self, operation):
        return "primary" if operation.upper()=="WRITE" else "replica"
