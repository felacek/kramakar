import pymongo as pm
def run():
    hostName = 'localhost'
    dbPort = 27017
    client = pm.MongoClient("mongodb://%s:%s" % (hostName, dbPort))
    db = client["database"]
    users = db["users"]
    things = db["things"]
    users.delete_many({})
    things.delete_many({})

run()
