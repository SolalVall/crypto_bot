from werkzeug.security import generate_password_hash, check_password_hash

class User:

    def __init__(self, name, email, password=None): 
        self.username = name
        self.email = email
        self.authenticated = False

        #Check if class is istanciate with password argument or if a user give a blank password
        if password == "" or password is None:
            self.password = password
        else:
            self.hash_password(password)

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password_hashed, password_inserted):
        return check_password_hash(password_hashed, password_inserted)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
