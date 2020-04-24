import pymongo as pm
import urllib.parse as up

def run():
    hostName = 'mongo_mongo_1'
    dbPort = 27017
    un = up.quote_plus('root')
    pa = up.quote_plus('example')
    client = pm.MongoClient("mongodb://%s:%s@%s:%s" % (un, pa, hostName, dbPort))
    db = client["database"]
    users = db["users"]
    things = db["things"]
    print("db skeleton created")

    user = {"_id" : 0, "name": "default", "passwd": "", "owns": {}, "buy": {}, "sell": {}}

    thingsd = [
        {"name": "sur1", "price": 4, "coef": 1.05, "buyable": True, "sellable": True, "produces": None},
        {"name": "money", "price": 1, "coef": 1, "buyable": False, "sellable": False, "produces": None},
        {"name": "sur2", "price": 2, "coef": 1.2, "buyable": True, "sellable": True, "produces": None},
        {"name": "points", "price": 0, "coef": 1, "buyable": False, "sellable": False, "produces": None},
        {"name": "fab1", "price": 10, "coef": 1.2, "buyable": True, "sellable": False, "produces": "sur1"},
        {"name": "fab2", "price": 20, "coef": 1.3, "buyable": True, "sellable": False,"produces": "sur2"}
    ]

    u = users.insert_one(user)
    print(u.inserted_id)
    t = things.insert_many(thingsd)
    print(t.inserted_ids)
