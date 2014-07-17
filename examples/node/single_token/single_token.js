// Assumes that you have a token already. Tokens can be pre-generated and managed from the AC admin console.
var https = require('https');

var STORE_DOMAIN = '<< YOUR STORE DOMAIN >>';
var ACCESS_TOKEN = '<< YOUR ACCESS TOKEN >>';

var requestOptions = {
  host: STORE_DOMAIN,
  port: 443,
  path: "/api/v1/products",
  method: "GET",
  headers: {
    "X-AC-Auth-Token": ACCESS_TOKEN
  },
  rejectUnauthorized: false
};

var req = https.request(requestOptions, function(res) {

  var data = '';

  res.on('data', function(chunk) {
    data += chunk;
  });

  res.on('end', function() {
    var productList = JSON.parse(data);

    for(var i = 0, len = productList.products.length; i < len; i++) {
      console.log(productList.products[i].item_name + ": " + productList.products[i].price);
    }
  });

});

req.end();