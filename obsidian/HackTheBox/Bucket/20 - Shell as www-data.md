## Apache Virtual Host
* Port 8000  == running as root*
```Bash
www-data@bucket:/etc/apache2/sites-enabled$ grep -v '#' 000-default.conf 
<VirtualHost 127.0.0.1:8000>
	<IfModule mpm_itk_module>
		AssignUserId root root
	</IfModule>
	DocumentRoot /var/www/bucket-app
</VirtualHost>

<VirtualHost *:80>
	DocumentRoot /var/www/html
	RewriteEngine On
	RewriteCond %{HTTP_HOST} !^bucket.htb$
	RewriteRule /.* http://bucket.htb/ [R]
</VirtualHost>
<VirtualHost *:80>
	# if server name is s3.bucket.htb 4566 == Docker (LocalStack)
	ProxyPreserveHost on
	ProxyPass / http://localhost:4566/
	ProxyPassReverse / http://localhost:4566/
	<Proxy *>
		 Order deny,allow
		 Allow from all
	 </Proxy>
	ServerAdmin webmaster@localhost
	ServerName s3.bucket.htb

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
```