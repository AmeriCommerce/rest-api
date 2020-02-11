Known Issues
============

Irregularly Typed Fields
------------------------

Some fields may not behave as expected when used in the query syntax due to their types being incorrect. Unfortunately, this isn't a problem with the API itself, but instead with the underlying data.

The fields that have been identified with this issue so far are as follows:

* [shipping_providers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/shipping_providers.md)
	* `markup_amount`
* [users](https://github.com/AmeriCommerce/rest-api/blob/master/resources/users.md)
	* `last_login_attempt_at`
	* `last_login_at`
* [products](https://github.com/AmeriCommerce/rest-api/blob/master/resources/products.md)
	* `length`
	* `height`
	* `width`
