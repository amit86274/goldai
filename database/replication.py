
class ReplicationManager:
    def replicate(self, record, replicas):
        return {"replicas": replicas, "record": record, "status": "replicated"}
