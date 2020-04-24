import player
import problem
import json
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
            pl = player.Player(data["name"], data["passwd"], "reg")
            res["code"]=1
            res["msg"]="Registration successful."
            res["name"]=pl.name
            res["owns"]=pl.owns
            res["token"]=pl.token
        except ValueError as e:
            res["code"]=0
            res["msg"]=e.args[0]
    if(path == '/sendData'):
        try:
            pl = player.Player(None, None, data["token"])
            pl.toBuy = data["buy"]
            pl.toSell = data["sell"]
            pl.buy()
            pl.sell()
            res["code"] = 1
            res["msg"] = pl.msg
            res["owns"] = pl.owns
        except ValueError as e:
            res["code"] = 0
            res["msg"] = e.args[0]
    if(path == '/logIn'):
        try:
            pl = player.Player(data["name"], data["passwd"], "log")
            res["code"]=1
            res["msg"]="Registration successful."
            res["name"]=pl.name
            res["owns"]=pl.owns
            res["token"]=pl.token
        except ValueError as e:
            res["code"]=0
            res["msg"]=e.args[0]
    if(path == '/logOut'):
        try:
            pl = player.Player(None, None, data["token"])
            pl.logout()
            res["code"] = 1
            res["msg"] = "Logout successful"
        except ValueError as e:
            res["code"] = 0
            res["msg"] = e.args[0]
    if(path == '/answer'):
        try:
            pr = problem.Problem(data["id"])
            ch = pr.check(data["answer"])
            res["msg"] = "Answer incorrect"
            if (ch):
                pl = player.Player(None, None, data["token"])
                pl.owns["money"] += pr.worth
                pl.update()
                res["msg"] = "Answer correct"
            res["code"] = 1
        except ValueError as e:
            res["code"] = 0
            res["msg"] = e.args[0]
            
    return json.dumps(res)
