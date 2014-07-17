<?php

require 'config.php';

class ApiClient
{
  public function startNegotiation($returnUrl) {
    return "https://" . AC_STORE_DOMAIN . "/api/oauth?client_id=" . AC_APP_ID 
      . "&scope=" . AC_APP_SCOPE . "&redirect_uri=" . $returnUrl;
  }

  public function getToken($auth_id, $code, $return_url) {
    $sig = $this->createSignature(AC_APP_SECRET, $code, AC_APP_ID, AC_APP_SCOPE, strtolower($return_url));
    $arr = array(
      'client_id' => AC_APP_ID,
      'auth_id' => $auth_id,
      'signature' => $sig
    );
    $content = json_encode($arr);
    $curl = curl_init('https://' . AC_STORE_DOMAIN . '/api/oauth/access_token');

    curl_setopt($curl, CURLOPT_HEADER, false);
    curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $content);
    // If using dev certificate
    // curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

    $json = curl_exec($curl);
    $status = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    if($status != 200) {
      die("Error: call to getToken failed with status $status and response content: $json");
    }

    curl_close($curl);

    $response = json_decode($json, true);
    return $response;
  }

  public function getProductList($token, $page = 1) {
    $curl = curl_init('https://' . AC_STORE_DOMAIN . '/api/v1/products?page=' . $page);

    curl_setopt($curl, CURLOPT_HEADER, false);
    curl_setopt($curl, CURLOPT_HTTPHEADER, array('X-AC-Auth-Token: ' . $token));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    // If using dev certificate
    // curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

    $json = curl_exec($curl);
    $status = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    if($status != 200) {
      die("Error: call to getProductList failed with status $status and response content: $json");
    }

    curl_close($curl);

    $response = json_decode($json, true);
    return $response;
  }

  private function createSignature() {
    $combined = implode("", func_get_args());
    return hash("sha256", $combined);
  }
}

?>