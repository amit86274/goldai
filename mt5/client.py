
import threading
from .connection import ConnectionManager
from .logger import get_logger

class MT5Client:
    def __init__(self,mt5_api):
        self.api=mt5_api
        self.log=get_logger()
        self.lock=threading.RLock()
        self.connection=ConnectionManager(mt5_api)

    def initialize(self):
        with self.lock:
            return self.connection.initialize()

    def login(self,login,password,server):
        with self.lock:
            if not self.api.login(login=login,password=password,server=server):
                raise RuntimeError(f"Login failed: {self.api.last_error()}")
            self.log.info("Logged in")
            return True

    def account_info(self):
        with self.lock:
            info=self.api.account_info()
            return info._asdict() if info else None

    def symbols(self):
        with self.lock:
            return self.api.symbols_get()

    def symbol_select(self,symbol):
        with self.lock:
            return self.api.symbol_select(symbol,True)

    def tick(self,symbol):
        with self.lock:
            tick=self.api.symbol_info_tick(symbol)
            return tick._asdict() if tick else None

    def candles(self,symbol,timeframe,count):
        with self.lock:
            return self.api.copy_rates_from_pos(symbol,timeframe,0,count)

    def shutdown(self):
        with self.lock:
            self.connection.shutdown()
