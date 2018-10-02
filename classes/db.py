import re
import pprint
from werkzeug.security import generate_password_hash, check_password_hash
from user import User
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
                        "authenticated": True}
            self.new_user_id = self.cryptobot_users.insert_one(new_user).inserted_id 

    def get_user(self, user_id):
        get_user = self.cryptobot_users.find_one({"email": user_id})
        user_infos = User(get_user['username'], get_user['email'])
        user_infos.authenticated = get_user['authenticated']
        return user_infos

    def verify_user(self, pseudo, password_inserted):
        #Check in DB if pseudo exist and check creds if true
        get_user = self.cryptobot_users.find_one({"username": pseudo})
        if get_user is None:
            errorMessage = "This username doesn't exist !" 
            return errorMessage
        else:
            password_check = check_password_hash(get_user['password'], password_inserted)
            #If password is OK return a user instance
            if password_check is True:
                self.cryptobot_users.find_and_modify(query={'username': pseudo}, update={"$set": {'authenticated': True}}, upsert=False, full_response= True)
                user_infos = User(get_user['username'], get_user['email'])
                user_infos.authenticated = True
                return user_infos
            else:
                errorMessage = "Password is not correct Dude !"
                return errorMessage
