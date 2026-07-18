
import secrets

class APIKeyManager:
    def generate(self, prefix="gai"):
        return f"{prefix}_{secrets.token_hex(16)}"

    def validate(self, key):
        return isinstance(key, str) and "_" in key
