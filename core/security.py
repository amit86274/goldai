
class SecurityMiddleware:
    def authorize(self,token):
        return bool(token)
