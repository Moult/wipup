import eadrax.tools

class Authenticator(eadrax.tools.Authenticator):

    def get_authenticated_id(self):
        pass

    def authenticate(self, id):
        pass

class Encryptor(eadrax.tools.Encryptor):

    def encrypt_password(self, password):
        pass

    def is_same_password(self, password, encrypted_password):
        pass
