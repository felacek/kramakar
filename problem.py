import pymongo as pm
import urllib.parse as up

class Problem:

    def __init__(self, num)
        hostName = 'mongo_mongo_1' 
        dbPort = 27017
        un = up.quote_plus('root')
        pa = up.quote_plus('example')
        client = pm.MongoClient("mongodb://%s:%s@%s:%s" % (un, pa, hostName, dbPort))
        db = client["database"]
        self.__problems = db["problems"]
        
        if (num == "add"):
            return

        self.pr = self.__problems( {"_id": num} )
        if (self.pr == None):
            raise ValueError('Problem does not exist')
            return
        self.load()
        return

    def load(self):
        self.num = self.pr["_id"]
        self.question = self.pr["question"]
        self.__answer = self.pr["answer"]
        self.worth = self.pr["worth"]

    def check(self, answer)
        return self.__answer == int(answer)

    def add(self, num, question, answer, worth):
        if (self.__problems( {"_id": num} )):
            raise ValueError('Problem already exists')
            return
        self.num = num
        self.question = question
        self.__answer = answer
        self.worth = worth
        self.__problems.insert_one({"_id": self.num, "question": self.question, "answer": self.answer, "worth": self.worth})
