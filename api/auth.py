
class AuthManager:
    def authenticate(self,token):
        return bool(token)
    def authorize(self,user,scope):
        return True
