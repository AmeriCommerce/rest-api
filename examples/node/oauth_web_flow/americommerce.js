var https = require('https'),
		crypto = require('crypto'),
		util = require('util'),
		config = require('./config');

function createSignature() {
	var args = Array.prototype.slice.call(arguments),
			combined = args.join(""),
			sha256 = crypto.createHash('sha256');

	return sha256.update(combined, 'utf8').digest('hex');
}

exports.startNegotiation = function(returnUrl) {
	return util.format("https://%s/api/oauth?app_id=%d&scope=%s&redirect_url=%s",
		config.storeDomain, config.appId, config.appScope, returnUrl);
};

exports.getToken = function(tempData, callback) {
	var sig = createSignature(config.appSecret, tempData.code, config.appId, config.appScope, tempData.returnUrl.toLowerCase());
	var outgoingData = JSON.stringify({
		'app_id': config.appId,
		'auth_id': tempData.authId,
		'signature': sig
	});
	var requestOptions = {
		host: config.storeDomain,
		port: 443,
		path: '/api/oauth/access_token',
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'Content-Length': Buffer.byteLength(outgoingData, 'utf8')
		},
		rejectUnauthorized: false
	};
	var req = https.request(requestOptions, function(res) {
		var data = '';

		res.on('data', function(chunk) {
			data += chunk;
		});
		res.on('end', function() {
			var d = JSON.parse(data);
			callback && callback(d);
		});
	});
	req.write(outgoingData);
	req.end();
};

exports.getProductList = function(token, page, callback) {
	var requestOptions = {
		host: config.storeDomain,
		port: 443,
		path: util.format("/api/v1/products?page=%d", page),
		method: 'GET',
		headers: {
			'X-AC-Auth-Token': token
		},
		rejectUnauthorized: false
	};
	var req = https.request(requestOptions, function(res) {
		var data = '';

		res.on('data', function(chunk) {
			data += chunk;
		});
		res.on('end', function() {
			var d = JSON.parse(data);
			callback && callback(d);
		});
	});
	req.end();
};