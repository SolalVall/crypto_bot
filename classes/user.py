from werkzeug.security import generate_password_hash, check_password_hash

class User:

    def __init__(self, name, email, password):
        self.username = name
        self.email = email
        self.authenticated = False
        if password != "":
            self.hash_password(password)
        else:
            self.password = password

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
