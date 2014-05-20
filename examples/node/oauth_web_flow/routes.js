var express = require('express');
var router = express.Router();
var api = require('./americommerce');

router.get('/', function(req, res) {
	if(!req.session.apiUser) {
		var returnUrl = 'http://localhost:3000/callback?r=' + encodeURIComponent('http://localhost:3000');
		var redirectUrl = api.startNegotiation(returnUrl);

		res.redirect(redirectUrl);
		return;
	}
	var token = req.session.apiUser;
	var page = req.query.page ? parseInt(req.query.page) : 1;

	api.getProductList(token.access_token, page, function(productList) {
		var nextButtonClass = ['next'];
		var previousButtonClass = ['previous'];

		if(!productList.next_page) {
			nextButtonClass.push('disabled');
		}
		if(!productList.previous_page) {
			previousButtonClass.push('disabled');
		}

		res.render('index', {
			productList: productList,
			nextButtonClass: nextButtonClass,
			previousButtonClass: previousButtonClass,
			currentPage: page
		});
	});
});

router.get('/callback', function(req, res) {
	var r = req.query.r;
	var originalReturnUrl = 'http://localhost:3000/callback?r=' + encodeURIComponent(r);
	var tempData = {
		authId: req.query.auth_id,
		code: req.query.code,
		returnUrl: originalReturnUrl
	};
	api.getToken(tempData, function(tokenData) {
		req.session.apiUser = tokenData;
		res.redirect(r);
	});
});

module.exports = router;