<?php

// reference: https://stackoverflow.com/questions/5647461/how-do-i-send-a-post-request-with-php
$url = 'http://34.82.101.212?KEY=0&is_this_flag？=123';
// $url = 'http://localhost/source.php?KEY=0&is_this_flag？=123';
$data = array(
    '😂' => 'aaa', // for checking
    '🤣' => 'bbb', // for checking
    '​😂' => '0e123', // for md5
    '🤣​' => '0e215962017', // for md5
);
// use key 'http' even if you send the request to https://...
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);
$context  = stream_context_create($options);
srand(20191231 + 20200101 + time());
$result = file_get_contents($url, false, $context);
if ($result === FALSE) { /* Handle error */ }

/*

IMPORTANT !!!
random_int(1,128) is not predictable even after srand(...);

use KEY=0 to get rid of the effect of random_int(1,128)

*/

$mystr = 'Happy';
$mystr .= ' New';
$mystr .= '  Year⁠!~~~';
$array2 = str_split($mystr, 1);
$array3 = str_split("0", 1);

$numbers = explode(" ", explode("\n", $result)[4]);
$flag = "";
foreach(explode(" ", explode("\n", $result)[4]) as $x){
    if($x === "") break;
    $flag .= chr(@strval($x ^ rand() ^ $array2[rand() % count($array2)] ^ ($array3[rand() % count($array3)] * random_int(1,128))));
}

var_dump($flag);
# might have to try many times since our time() may be less than the server's time() due to network latency
# BAMBOOFOX{WHY_THERE_ARE_UNICODE_LA}
