from werkzeug.security import generate_password_hash, \
     check_password_hash
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.hash_password(password)

    def hash_password(self, password):
        self.password_hashed = generate_password_hash(password)
        
    
