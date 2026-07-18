
class JWTAuth:
    def issue_token(self, user_id):
        return f"jwt-token-{user_id}"

    def verify_token(self, token):
        return token.startswith("jwt-token-")
