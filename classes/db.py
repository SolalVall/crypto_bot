import re
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
        #Verify register form
        #Iterate over attributes of User Object (check empty field)
        for attribute, value in user.__dict__.iteritems():
            if value == "" :
                errorMessage = "Please insert a value for " + attribute
                return errorMessage

        #Check quality of field
        regex_pseudo = re.compile(r'^[A-Za-z0-9_-]{5,20}$')
        regex_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        regex_password = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
        if regex_pseudo.search(user.username) is None:
            errorMessage = "Invalid Pseudo (5-20 characters long / - _ are authorized)"
            return errorMessage
        elif regex_email.search(user.email) is None:
            errorMessage = "Please insert a valid mail adress"
            return errorMessage
        elif regex_password.search(user.password) is None:
            errorMessage = "Password must have at least 8 characters"
            return errorMessage
            
        #Add user to db
        else:
            new_user = {"username": user.username,
                        "email": user.email,
                        "password": user.password,
                        "authenticated": user.authenticated}
            self.new_user_id = self.cryptobot_users.insert_one(new_user).inserted_id 
