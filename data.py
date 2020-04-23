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
        {"_id": 3, "name": "sur1", "price": 4, "static": False, "buyable": True, "sellable": True, "produces": None},
        {"_id": 1, "name": "money", "price": 1, "static": True, "buyable": False, "sellable": False, "produces": None},
        {"_id": 4, "name": "sur2", "price": 2, "static": False, "buyable": True, "sellable": True, "produces": None},
        {"_id": 2, "name": "points", "price": 0, "static": True, "buyable": False, "sellable": False, "produces": None},
        {"_id": 5, "name": "fab1", "price": 10, "static": False, "buyable": True, "sellable": False, "produces": 3},
        {"_id": 6, "name": "fab2", "price": 20, "static": False, "buyable": True, "sellable": False, "produces": 4}
    ]

    u = users.insert_one(user)
    print(u.inserted_id)
    t = things.insert_many(thingsd)
    print(t.inserted_ids)
