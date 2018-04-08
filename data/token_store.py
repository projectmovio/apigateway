

class TokenStore(object):

    def __init__(self):
        self.token_store = []

    def add_token(self, token):
        self.token_store.append(token)

    def validate_token(self, token):
        return token in self.token_store

