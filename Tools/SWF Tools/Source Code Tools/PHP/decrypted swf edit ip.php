<?php
$open = file_get_contents("fm.swf");

$ip=Array('4.11.0.0','192.168.0.1','192.168.0.2');
$pattern = '/(?:[0-9]{1,3}\.){3}[0-9]{1,3}/i';
$dei=$_GET["IP"];
preg_match_all($pattern, $open, $results);

foreach ($results as $inl) {
foreach ($inl as $in) {

if (!in_array($in, $ip)) {
$newip=pack("C", strlen($in)).$in;
$ipx=pack("C", strlen($dei)).$dei;
$open=str_replace($newip, $ipx, $open);

}
}
}

$a_mk = fopen(time().".swf", "wb") or die("Unable to open file!");

fwrite($a_mk, $open);
fclose($a_mk);


echo $open;
?>