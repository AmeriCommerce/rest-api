var https = require('https'),
    crypto = require('crypto'),
    config = require('./config');

function ApiClient() {
}

ApiClient.prototype = {
  getToken: function(userData, callback) {
    startNegotiation(userData, function(tempData) {
      verify(tempData, function(token) {
        callback && callback(token);
      });
    });
  },

  getProductList: function(token, callback) {
    var requestOptions = {
      host: config.storeDomain,
      port: 443,
      path: '/api/v1/products',
      method: 'GET',
      headers: {
        'X-AC-Auth-Token': token.access_token
      }
      // if using development cert
      // rejectUnauthorized: false
    };
    var request = https.request(requestOptions, function(response) {
      var data = '';

      response.on('data', function(chunk) {
        data += chunk;
      });
      response.on('end', function() {
        var d = JSON.parse(data);
        callback && callback(d);
      });
    });
    request.end();
  }
};

function startNegotiation(userData, callback) {
  var sig = createSignature(config.appSecret, userData.username, userData.apiKey, config.appId, config.appScope, config.storeDomain);
  var outgoingData = JSON.stringify({
    'app_id': config.appId,
    'scope': config.appScope,
    'redirect_url': config.storeDomain,
    'username': userData.username,
    'signature': sig
  });
  var requestOptions = {
    host: config.storeDomain,
    port: 443,
    path: '/api/oauth',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(outgoingData, 'utf8')
    }
    // if using development cert
    // rejectUnauthorized: false
  };
  var request = https.request(requestOptions, function(response) {
    var data = '';

    response.on('data', function(chunk) {
      data += chunk;
    });
    response.on('end', function() {
      var d = JSON.parse(data.toString());
      callback && callback(d);
    });
  });
  request.write(outgoingData);
  request.end();
}

function verify(tempData, callback) {
  var sig = createSignature(config.appSecret, tempData.code, config.appId, config.appScope, config.storeDomain);
  var outgoingData = JSON.stringify({
    'app_id': config.appId,
    'auth_id': tempData.auth_id,
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
    }
    // if using development cert
    // rejectUnauthorized: false
  };
  var request = https.request(requestOptions, function(response) {
    var data = '';

    response.on('data', function(chunk) {
      data += chunk;
    });
    response.on('end', function() {
      var d = JSON.parse(data);
      callback && callback(d);
    });
  });
  request.write(outgoingData);
  request.end();
}

function createSignature() {
  var args = Array.prototype.slice.call(arguments),
      combined = args.join(""),
      sha256 = crypto.createHash('sha256');

  return sha256.update(combined, 'utf8').digest('hex');
}

exports.ApiClient = ApiClient;