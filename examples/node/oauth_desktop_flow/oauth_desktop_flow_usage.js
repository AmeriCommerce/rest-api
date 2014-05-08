var async = require('async'),
		readline = require('readline'),
		acapi = require('./oauth_desktop_flow');

var APP_ID = 1,
		APP_SCOPE = 'catalog',
		APP_SECRET = 'YOUR_SECRET_DO_NOT_EXPOSE_THIS',
		STORE_DOMAIN = 'your_store_domain.com';


var rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

var locals = {},
		productList;

async.series([

	function(callback) {
		rl.question('Username: ', function(answer) {
			locals.username = answer;
			callback();
		});
	},

	function(callback) {
		rl.question('User API Key: ', function(answer) {
			locals.key = answer;
			callback();
		});
	},

	function(callback) {
		var options = {
			username: locals.username,
			key: locals.key,
			secret: APP_SECRET,
			appId: APP_ID,
			appScope: APP_SCOPE,
			storeDomain: STORE_DOMAIN
		};
		acapi.getAccessToken(options, function(err, result) {
			locals.accessToken = result.accessToken;
			callback();
		});
	},

	function(callback) {
		var options = {
			storeDomain: STORE_DOMAIN,
			accessToken: locals.accessToken
		};
		acapi.getProductList(options, function(result) {
			productList = result;
			callback();
		});
	}

], function(err) {
	if(err) console.log(err);
	rl.close();
	for(var i = 0, len = productList.products.length; i < len; i++) {
		console.log(productList.products[i].item_name + ": " + productList.products[i].price);
	}
});