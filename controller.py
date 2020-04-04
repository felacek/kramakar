import player
import thing
import json
from collections import namedtuple

def parse(data):
    try:
        return json.loads(data.decode("utf-8"))
    except:
        return 0

def decode(path, body):
    data = parse(body)
    if(path == '/registerNewUser'):
        try:
            pl = player.Player(data["name"], data["passwd"])
            return '{"code": 1, "msg": "Registration successful."}'
        except ValueError as e:
            return e.args
