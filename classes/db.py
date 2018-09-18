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
        #Iterate over attributes of User Object
        for attribute, value in user.__dict__.iteritems():
            print attribute, value
            if value == "" :
                errorMessage = "Please insert a value for " + attribute
                return errorMessage
        else:
            #Add user to db
            new_user = {"username": user.username,
                        "email": user.email,
                        "password": user.password}
            self.new_user_id = self.cryptobot_users.insert_one(new_user).inserted_id 
