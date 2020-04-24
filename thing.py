import pymongo as pm
import math
import urllib.parse as up

class Thing:

    def __init__(self, name):
        hostName = 'mongo_mongo_1'
        dbPort = 27017
        un = up.quote_plus('root')
        pa = up.quote_plus('example')
        client = pm.MongoClient("mongodb://%s:%s@%s:%s" % (un, pa, hostName, dbPort))
        db = client["database"]
        self.__things = db["things"]

        self.it = self.__things.find_one( {"name" : name} )
        if (self.it == None):
            raise ValueError('Item does not exist')
            return
        self.load()
        return

    def load(self):
        self.name = self.it["name"]
        self.price = self.it["price"]
        self.coef = self.it["coef"]
        self.buyable = self.it["buyable"]
        self.sellable = self.it["sellable"]
        self.produces = self.it["produces"]

    def repbought(self):
        self.price = math.ceil(self.price*self.coef)
        self.__things.update_one( {'name': self.name}, {'$set': {'price': self.price} }, upsert = False)

    def repsold(self):
        self.price = math.floor(self.price/self.coef)
        self.__things.update_one({'name': self.name}, {'$set': {'price': self.price}}, upsert = False)

