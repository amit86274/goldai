
class RequestBuilder:
    def market(self,symbol,order_type,volume,price,sl,tp,magic=10001,comment="Gold-AI"):
        return {
            "symbol":symbol,
            "type":order_type,
            "volume":volume,
            "price":price,
            "sl":sl,
            "tp":tp,
            "magic":magic,
            "comment":comment
        }
