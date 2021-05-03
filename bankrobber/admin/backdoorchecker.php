<?php

include('../link.php');

include('auth.php');



$username = base64_decode(urldecode($_COOKIE['username']));

$password = base64_decode(urldecode($_COOKIE['password']));

$bad 	  = array('$(','&');

$good 	  = "ls";



if(strtolower(substr(PHP_OS,0,3)) == "win"){

	$good = "dir";

}



if($username == "admin" && $password == "Hopelessromantic"){

	if(isset($_POST['cmd'])){

			// FILTER ESCAPE CHARS

			foreach($bad as $char){

				if(strpos($_POST['cmd'],$char) !== false){

					die("You're not allowed to do that.");

				}

			}

			// CHECK IF THE FIRST 2 CHARS ARE LS

			if(substr($_POST['cmd'], 0,strlen($good)) != $good){

				die("It's only allowed to use the $good command");

			}



			if($_SERVER['REMOTE_ADDR'] == "::1"){

				system($_POST['cmd']);

			} else{

				echo "It's only allowed to access this function from localhost (::1).<br> This is due to the recent hack attempts on our server.";

			}

	}

} else{

	echo "You are not allowed to use this function!";

}

?>
