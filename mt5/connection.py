
from .logger import get_logger
log=get_logger()

class ConnectionManager:
    def __init__(self,api):
        self.api=api
    def initialize(self):
        ok=self.api.initialize()
        if not ok:
            raise RuntimeError("MT5 initialize failed")
        log.info("MT5 initialized")
        return True
    def shutdown(self):
        self.api.shutdown()
        log.info("MT5 shutdown")
