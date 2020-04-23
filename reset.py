import urllib.parse as up
import pymongo as pm

def run():
    hostName = 'mongo_mongo_1'
    dbPort = 27017
    un = up.quote_plus('root')
    pa = up.quote_plus('example')
    client = pm.MongoClient("mongodb://%s:%s@%s:%s" % (un, pa, hostName, dbPort))
    db = client["database"]
    users = db["users"]
    things = db["things"]
    users.delete_many({})
    things.delete_many({})

run()
