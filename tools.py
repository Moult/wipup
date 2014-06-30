import eadrax.tools

class Authenticator(eadrax.tools.Authenticator):

    def __init__(self, request):
        self.request = request

    def get_authenticated_id(self):
        session = self.request.get_session()
        if 'id' in session:
            return session['id']
        return None

    def authenticate(self, id):
        session = self.request.get_session()
        session['id'] = id
        self.request.set_session(session)

    def deauthenticate(self):
        session = self.request.get_session()
        session['id'] = None
        self.request.set_session(session)

class Encryptor(eadrax.tools.Encryptor):

    def encrypt_password(self, password):
        pass

    def is_same_password(self, password, encrypted_password):
        pass
