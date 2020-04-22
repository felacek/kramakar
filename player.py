import pymongo as pm
import secrets
import bcrypt
import things

class Player:

    def __init__(self, name, passwd, token):
        self.__hostName = 'localhost' 
        self.__dbPort = 27017 
        self.__client = pm.MongoClient("mongodb://%s:%s" % (self.__hostName, self.__dbPort))
        self.__db = self.__client["database"]
        self.__users = self.__db["users"]
        self.err = 0
        self.msg = []

        if (token == "reg"):
            if(self.__users.find_one( {"name" : name} )):
                raise ValueError('Player already exists.')
                return

            self.name = name
            self.__passwd = bcrypt.hashpw(passwd.encode("utf-8"), bcrypt.gensalt(12)) #hash!!
            self.owns = {
                "money":    0,
                "sur1":     0,
                "sur2":     0,
                "points":   0,
                "fab1":     0,
                "fab2":     0
            }
            self.toBuy = {
                "sur1":     0,
                "sur2":     0,
                "fab1":     0,
                "fab2":     0
            }
            self.toSell = {
                "sur1":     0,
                "sur2":     0
            }
            self.token = secrets.token_urlsafe(20)
            add = self.__users.insert_one({"name": self.name, "passwd": self.__passwd, "owns": self.owns, "buy": self.toBuy, "sell": self.toSell, "token": self.token})
            return
        elif (token == "log"):
            self.pl = self.__users.find_one( {"name" : name} ) 
            if (self.pl == None):
                raise ValueError('Player does not exist')
                return

            if (bcrypt.checkpw(passwd.encode("utf-8"), self.pl["passwd"])):
                self.load()
                self.token = secrets.token_urlsafe(20)
                self.pl
                return
            else:
                raise ValueError('Wrong password')
        else:
            self.pl = self.__users.find_one( {"token": token} )
            if (self.pl == None):
                raise ValueError('Player does not exist')
                return
            self.load()
        return

    def load(self):
        self.name = self.pl["name"]
        self.__passwd = self.pl["passwd"]
        self.owns = self.pl["owns"]
        self.toBuy = self.pl["buy"]
        self.toSell = self.pl["sell"]

    def buy(self):
        for x in self.toBuy:
            try:
                thing = things.get(x)
                if (thing.buyable):
                    newmoney = self.owns["money"] - thing * self.toBuy[x]
                    if (newmoney >= 0):
                        self.owns["money"] = newmoney
                        self.owns[x] += self.toBuy[x]
                        self.toBuy[x] = 0
                    else:
                        self.msg[self.err] = ("Cannot buy %s, not enough money." % x)
                        self.err+= 1
                else:
                    self.msg[self.err] = ("Cannot buy %s" % x)
                    self.err+= 1
            except ValueError as e:
                self.msg[self.err] = e.args[0]
                self.err+= 1
        self.pl["owns"] = self.owns
        self.pl["buy"] = self.toBuy


    def sell(self):
        for x in self.toSell:
            try:
                thing = things.get(x)
                if (thing.sellable):
                    newamount = self.owns[x] - self.toSell[x]
                    if (newamount >=0):
                        self.owns["money"] += thing.price * self.toSell[x]
                        self.owns[x] = newamount
                        self.toSell[x] = 0
                    else:
                        self.msg[self.err] = ("Cannot sell %s, not enough resources." % x)
                        self.err+= 1
                else:
                    self.msg[self.err] = ("Cannot sell %s" % x)
                    self.err+= 1
            except ValueError as e:
                self.msg[self.err] = e.args[0]
                self.err+= 1
        self.pl["owns"] = self.owns
        self.pl["sell"] = self.toSell
