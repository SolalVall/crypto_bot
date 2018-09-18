class Database:
    from pymongo import MongoClient

    def __init__(self):
        #Initialize connection
        self.client = self.MongoClient('localhost', 27017)
        #Create db
        self.db = self.client.cryptobot_database
        #Create collection
        self.cryptobot_users = self.db.cryptobot_users

    def create_user(self, user):
        new_user = {"username": user.name,
                    "email": user.email,
                    "password": user.password_hashed}
        self.new_user_id = self.cryptobot_users.insert_one(new_user).inserted_id 
