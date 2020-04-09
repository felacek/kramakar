import pymongo as pm
import secrets

class Player:

    def __init__(self, name, passwd):
        self.__hostName = 'localhost' 
        self.__dbPort = 27017 
        self.__client = pm.MongoClient("mongodb://%s:%s" % (self.__hostName, self.__dbPort))
        self.__db = self.__client["database"]
        self.__users = self.__db["users"]
        if(self.__users.find_one( {"name" : name} )):
            raise ValueError('Player already exists.')
            return
        self.name = name
        self.passwd = passwd #hash!!
        self.owns = {
            "money":    10,
            "sur1":     0,
            "sur2":     35,
            "points":   1,
            "fab1":     0,
            "fab2":     2
        }
        self.toBuy = {
            "sur1":     2,
            "sur2":     0,
            "fab1":     1,
            "fab2":     0
        }
        self.toSell = {
            "sur1":     0,
            "sur2":     10
        }
        self.token = secrets.token_urlsafe(20)
        add = self.__users.insert_one({"name": self.name, "passwd": self.passwd, "owns": self.owns, "buy": self.toBuy, "sell": self.toSell, "token": self.token}).inserted_id
        return
        # add function to register, leave init only to create variable

    def buy(self):
        for x in self.toBuy: 
            price = prices.get(x)
            newmoney = self.owns["money"] - price * self.toBuy[x]
            if (newmoney >= 0):
                self.owns["money"] = newmoney
                self.owns[x] += self.toBuy[x]
            else:
                print("Cannot buy %s, not enough money" % x)
            self.toBuy[x] = 0


    def sell(self):
        for x in self.toSell:
            price = prices.get(x)
            newamount = self.owns[x] - self.toSell[x]
            if (newamount >=0):
                self.owns["money"] += price * self.toSell[x]
                self.owns[x] = newamount
            else:
                print("Cannot sell %s, not enough resources" % x)
            self.toSell[x] = 0
