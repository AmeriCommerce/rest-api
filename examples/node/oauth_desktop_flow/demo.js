var americommerce = require('./americommerce');

var api = new americommerce.ApiClient();

var userData = {
  username: "<< USER NAME >>",
  apiKey: "<< USER API KEY >>"
};

api.getToken(userData, function(token) {

  api.getProductList(token, function(productList) {
    for(var i = 0, len = productList.products.length; i < len; i++) {
      console.log(productList.products[i].item_name + ": " + productList.products[i].price);
    }
  });

});