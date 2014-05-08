var async = require('async'),
    https = require('https'),
    crypto = require('crypto');

exports.getAccessToken = function(options, next) {

  var result = {},
      locals = {};

  async.series([

    function(callback) {
      var sig = createSignature(options.secret, options.username, options.key, options.appId, options.appScope, options.storeDomain);
      var outgoingData = JSON.stringify({
        'app_id': options.appId,
        'scope': options.appScope,
        'redirect_url': options.storeDomain,
        'username': options.username,
        'signature': sig
      });
      var requestOptions = {
        host: options.storeDomain,
        port: 443,
        path: '/api/oauth',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(outgoingData, 'utf8')
        }
      };
      var request = https.request(requestOptions, function(response) {
        var data = '';
        response.on('data', function(chunk) {
          data += chunk;
        });
        response.on('end', function() {
          var d = JSON.parse(data.toString());
          locals.authId = d.auth_id;
          locals.code = d.code;
          callback();
        });
      });
      request.write(outgoingData);
      request.end();
    },

    function(callback) {
      var sig = createSignature(options.secret, locals.code, options.appId, options.appScope, options.storeDomain);
      var outgoingData = JSON.stringify({
        'app_id': options.appId,
        'auth_id': locals.authId,
        'signature': sig
      });
      var requestOptions = {
        host: options.storeDomain,
        port: 443,
        path: '/api/oauth/access_token',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(outgoingData, 'utf8')
        }
      };
      var request = https.request(requestOptions, function(response) {
        var data = '';
        response.on('data', function(chunk) {
          data += chunk;
        });
        response.on('end', function() {
          var d = JSON.parse(data);
          result.accessToken = d.access_token;
          result.refreshToken = d.refresh_token;
          result.expires = d.expires;
          callback();
        });
      });
      request.write(outgoingData);
      request.end();
    }
  ], function(err) {
    if(err) return next(err);
    next(undefined, result);
  });

};

exports.getProductList = function(options, next) {
  var requestOptions = {
    host: options.storeDomain,
    port: 443,
    path: '/api/v1/products',
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'X-AC-Auth-Token': options.accessToken
    }
  };
  var request = https.request(requestOptions, function(response) {
    var data = '';
    response.on('data', function(chunk) {
      data += chunk;
    });
    response.on('end', function() {
      var d = JSON.parse(data);
      next(d);
    });
  });
  request.end();
};

function createSignature() {
  var args = Array.prototype.slice.call(arguments),
      combined = args.join(""),
      sha256 = crypto.createHash('sha256');

  return sha256.update(combined, 'utf8').digest('hex');
}