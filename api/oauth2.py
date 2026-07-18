
class OAuth2Provider:
    def authorize(self, client_id, scopes=None):
        return {"client_id": client_id, "scopes": scopes or [], "authorized": True}

    def exchange_code(self, code):
        return {"access_token": f"oauth_{code}", "token_type": "Bearer"}
