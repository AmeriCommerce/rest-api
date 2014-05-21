<?php

require 'americommerce.php';

session_start();

$api = new ApiClient();

parse_str($_SERVER['QUERY_STRING'], $qs);

$r = $qs['r'];
$original_return_url = 'http://localhost/php_demo/callback.php?r=' . urlencode('http://localhost/php_demo');
$auth_id = $qs['auth_id'];
$code = $qs['code'];

$token = $api->getToken($auth_id, $code, $original_return_url);

$_SESSION['api_user'] = $token;

header("Location: " . $r);
die();

?>