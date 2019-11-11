<?php

require 'americommerce.php';

session_start();

$api = new ApiClient();

if(array_key_exists('api_user', $_SESSION) && !empty($_SESSION['api_user'])) {
  $token_data = $_SESSION['api_user'];
  parse_str($_SERVER['QUERY_STRING'], $qs);

  $page = array_key_exists('page', $qs) ? $qs['page'] : 1;
  $product_list = $api->getProductList($token_data['access_token'], $page);
  $next_page_class = array_key_exists('next_page', $product_list) ? 'next' : 'next disabled';
  $previous_page_class = array_key_exists('previous_page', $product_list) ? 'previous' : 'previous disabled';
}
else {
  $return_url = 'http://localhost/php_demo/callback.php?r=' . urlencode('http://localhost/php_demo');
  header("Location: " . $api->startNegotiation($return_url));
  die();
}

?>
<!DOCTYPE html>
<html>
<head>
  <title>Product List</title>
  <link rel="stylesheet" type="text/css" href="public/css/bootstrap.min.css"/>
  <link rel="stylesheet" type="text/css" href="public/css/bootstrap-theme.min.css"/>
</head>
<body>

  <div class="container">
    <h2>Product List</h2>

    <?php include 'pager.php'; ?>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>Id</th>
          <th>Item Name</th>
          <th>Item Number</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <?php for($i = 0; $i < count($product_list['products']); $i++) { ?>
          <?php $product = $product_list['products'][$i]; ?>
          <tr>
            <td><?= $product['id'] ?></td>
            <td><?= $product['item_name'] ?></td>
            <td><?= $product['item_number'] ?></td>
            <td><?= $product['price'] ?></td>
          </tr>
        <?php } ?>
      </tbody>
    </table>

    <?php include 'pager.php'; ?>
  </div>

</body>
</html>