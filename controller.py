import player
import thing
import json
import secrets
from collections import namedtuple

def parse(data):
    try:
        return json.loads(data.decode("utf-8"))
    except:
        return 0

def decode(path, body):
    data = parse(body)
    res = {"code": 0, "msg": ""}
    if(path == '/registerNewUser'):
        try:
            pl = player.Player(data["name"], data["passwd"])
            res["code"]=1
            res["msg"]="Registration successful."
            res["name"]=pl.name
            res["owns"]=pl.owns
            res["token"]=pl.token
        except ValueError as e:
            res["code"]=0
            res["msg"]=e.args
    return json.dumps(res)
