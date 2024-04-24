#!/usr/bin/python

import requests
import time
import sys
import os
from creds import creds
import other_creds

payload = {
        "mode": 191 if sys.argv[1] == 'login' else 193,
        "username": f"{creds('username')}",
        "password": f"{creds('password')}" if sys.argv[1] == 'login' else None,
        "a": int(time.time() * 1000),
        "producttype": 0,
    }

if sys.argv[1] == "login":
    if requests.post("https://campnet.bits-goa.ac.in:8090/login.xml", data=payload).status_code == 200:
        os.system("notify-send 'Successfully Connected to Wifi'")
elif sys.argv[1] == "logout":
    requests.post("https://campnet.bits-goa.ac.in:8090/logout.xml", data=payload)
