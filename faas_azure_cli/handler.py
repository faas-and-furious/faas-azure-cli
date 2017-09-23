import os
import json
from sh import az
from pathlib import Path
from io import StringIO
from collections import namedtuple

def _json_object_hook(d): 
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data): 
    return json.loads(data, object_hook=_json_object_hook)

def handle(st):
    token_path=str(Path.home()) + "/.azure/accessTokens.json"
    buf = StringIO()

    if not os.path.exists(token_path):
        username = os.environ['username']
        password = os.environ['password']
        tenant = os.environ['tenant']
        az.login('--service-principal', '-u', username, '-p', password, '--tenant', tenant)

    az.account.list('-o', 'json', _out=buf)

    accounts_obj = json2obj(buf.getvalue())

    print(accounts_obj[0].id)