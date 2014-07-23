<!DOCTYPE html>
<?php

define('AC_STORE_DOMAIN', '<< YOUR STORE DOMAIN >>');
define('AC_ACCESS_TOKEN', '<< YOUR ACCESS TOKEN >>');

$curl = curl_init('https://' . AC_STORE_DOMAIN . '/api/v1/products');

curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_HTTPHEADER, array('X-AC-Auth-Token: ' . AC_ACCESS_TOKEN));
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
// If using dev certificate
//curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$json = curl_exec($curl);
$status = curl_getinfo($curl, CURLINFO_HTTP_CODE);

if($status != 200) {
  die("Error: call to /api/v1/products failed with status $status and response content: $json");
}

curl_close($curl);

$response = json_decode($json, true);

?>
<html>
  <head>
    <title>Single Token PHP Demo</title>
  </head>
  <body>
    <ul>
      <?php foreach($response['products'] as $product) { ?>
      <li><?= $product['item_name'] ?> (<?= $product['price'] ?>)</li>
      <?php } ?>
    </ul>
  </body>
</html>