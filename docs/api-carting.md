API Carting
===========

This document is an overview of the process of creating a cart via the API, calculating shipping, and placing an order.

Creating a cart
---------------

```shell
POST /api/v1/carts
```

Returns a `201 Created` response with the new [cart resource](resources/carts.md) as the response body.

Add items to the cart
---------------------

```shell
POST /api/v1/carts/{id}/items
```

Returns a `200 OK` response with the [cart resource](resources/carts.md) as the response body.

### Request body

* `items` - (required) An array of items to add to the cart. Each item should have the following data:
	* `product_id` - (required) The item's ID.
	* `quantity` - (required) The amount of this item to add.
	* `variant_ids` - (optional) An array of variant IDs to apply for this item.
	* `personalizations` - (optional) An array of personalization data to apply for this item. Each personalization option should have the following data:
		* `personalization_id` - (required) The ID of the personalization question.
		* `answer` - (required) The answer to the personalization question.

#### Sample request data

```json
{
	"items": [
		{
			"product_id": 62,
			"quantity": 3,
			"variant_ids": [
				154,
				55,
				299
			],
			"personalizations": [
				{
					"personalization_id": 3,
					"answer": "hello world!"
				}
			]
		}
	]
}
```

Update items in the cart
------------------------

```shell
PUT /api/v1/carts/{id}/items
```

Returns a `200 OK` response with the [cart resource](resources/carts.md) as the response body.

### Request body

* `items` - (required) An array of items to modify. Each item should have the following data:
	* `cart_item_id` - (required) The ID of the cart item instance, as returned by the cart and cart item resources.
	* `quantity` - (required) The new quantity to set for this cart item.

#### Sample request data

```json
{
	"items": [
		{
			"cart_item_id": 345,
			"quantity": 2
		},
		{
			"cart_item_id": 347,
			"quantity": 1
		}
	]
}
```

Remove items from the cart
--------------------------

```shell
DELETE /api/v1/carts/{id}/items
```

Returns a `200 OK` response with the [cart resource](resources/carts.md) as the response body.

### Request body

The entire body for this request can be omitted to clear all cart items.

* `cart_item_ids` - (optional) An array of cart item IDs to remove from the cart.

#### Sample request data

```json
{
	"cart_item_ids": [
		345,
		347
	]
}
```

Calculate shipping
------------------

```shell
GET /api/v1/carts/{id}/shipping?city=Round+Rock&state=TX&postal_code=78681&country=US
```

Calculates the shipping rates applicable to this cart. Returns a `200 OK` response with a model specific to this endpoint as the response body (see sample response data below for details).

### Request parameters

* `city` - (required) The name of the destination city.
* `state` - (required) The name or abbreviation of the destination state/territory.
* `postal_code` - (required) The destination postal code.
* `country` - (required) The name or two letter abbreviation of the destination country.

### Sample response data

```json
{
  "total_count": 12,
  "rates": [
    {
      "shipping_provider_service_id": 0,
      "custom_shipping_method_id": 3,
      "provider": "Custom",
      "name": "3",
      "description": "Free Ground Shipping",
      "identifier": "Custom;3;Free Ground Shipping",
      "total_charges": 0.0,
      "lead_time": null
    },
    {
      "shipping_provider_service_id": 29,
      "custom_shipping_method_id": null,
      "provider": "USPS",
      "name": "Priority Mail",
      "description": "USPS Priority Mail",
      "identifier": "USPS;Priority Mail;USPS Priority Mail",
      "total_charges": 5.85,
      "lead_time": null
    },
    {
      "shipping_provider_service_id": 21,
      "custom_shipping_method_id": null,
      "provider": "FedEx",
      "name": "GROUND_HOME_DELIVERY",
      "description": "FedEx Home Delivery",
      "identifier": "FedEx;GROUND_HOME_DELIVERY;FedEx Home Delivery",
      "total_charges": 10.2,
      "lead_time": null
    },
    ...
  ]
}
```

Set shipping method
-------------------

```shell
PUT /api/v1/carts/{id}/shipping
```

Applies a shipping method to this cart and sets the shipping total. Returns a `200 OK` response with the [cart resource](resources/carts.md) as the response body.

### Request body

* `identifier` - (required) The shipping method `identifier` (as it is returned from the shipping `GET` request above)

### Sample request data

```json
{
  "identifier": "FedEx;GROUND_HOME_DELIVERY;FedEx Home Delivery"
}
```

Set Shipping Estimation Address
-------------------------------

```shell
PUT /api/v1/carts/{id}/shipping_estimation
```

Similar to the calculate shipping method above, however this sets the estimation address on the cart so that when the cart is returned, shipping will be calculated/estimated on the cart itself. This assumes that you have set a shipping method on the cart. Returns a `200 OK` response with the [cart resource](resources/carts.md) as the response body.

### Request body

* `city` - (optional) The city to use for estimating shipping
* `state_code` - (optional) The state to use for estimating shipping
* `postal_code` - (optional) The postal code to use for estimating shipping
* `country_code` - (optional) The country code to use for estimating shipping

### Sample request data

```json
{
  "city": "Beaumont",
  "state_code": "TX",
  "postal_code": "77701"
}
```

Set Coupon/Discount Code
------------------------

```shell
PUT /api/v1/carts/{id}/coupon_code
```

Applies a coupon/discount code to this cart and recalculates the total based on that code. Returns a `200 OK` response with the [cart resource](resources/carts.md) as the response body.

### Request body

* `coupon_code` - (required) The coupon code (string) to apply

### Sample request data

```json
{
  "coupon_code": "10PERCENTOFF"
}
```

Get available payment methods
-----------------------------

```shell
GET /api/v1/carts/{id}/payment_methods
```

Gets the available payment methods for this cart. Will always at least contain a `payment_method_id` of 0 for taking credit cards but not sending them through a gateway. Returns a `200 OK` response with a model specific to this endpoint as the response body (see sample response data below for details).

### Sample response data

```json
{
  "total_count": 5,
  "payment_methods": [
    {
      "payment_method_id": 14,
      "name": "IOU",
      "payment_type": "Custom"
    },
    {
      "payment_method_id": 13,
      "name": "Send Check or Money Order",
      "payment_type": "Custom"
    },
    {
      "payment_method_id": 0,
      "name": "Credit Card",
      "payment_type": "CreditCard"
    },
    {
      "payment_method_id": 6,
      "name": "Pay by Purchase Order",
      "payment_type": "Custom"
    },
    {
      "payment_method_id": 190,
      "name": "PayPal",
      "payment_type": "PayPalExpress"
    }
  ]
}
```

Get Cart With Updated Pricing
-----------------------------

```shell
GET /api/v1/carts/{id}/calculated
```

Gets the current state of a cart, ensuring that pricing, shipping, and discount totals are updated. Returns a `200 OK` response with the [cart resource](resources/carts.md) as the response body.


Place order
-----------

```shell
POST /api/v1/carts/{id}/place_order
```

Submits all of the cart information to process payment and create an order. Returns a `200 OK` response with a model specific to this endpoint as the response body (see sample response data below for details).

*At the time of this writing, some advanced features available on AmeriCommerce's checkout page might not be available here.*

### Request body

* `customer` - (required) Information about the [customer](resources/customers.md) to assign to this order.
	* `id` - (optional) The ID of an existing [customer](resources/customers.md). If omitted, a new customer will be created.
	* `first_name` - (required) Customer's first/given name.
	* `last_name` - (required) Customer's last/family name.
	* `email` - (required) Customer's email address. Must not already exist.
	* `company` - (optional) Customer's company.
	* `phone` - (optional) Customer's phone number.
	* `alternate_phone` - (optional) Customer's alternative phone number.
	* `fax` - (optional) - Customer's fax number.
* `billing_address` - (required) The [address](resources/addresses.md) to use for billing.
	* `id` - (optional) The ID of an existing [address](resources/addresses.md). If omitted, a new address will be created.
	* `name` - (required) The name of the person to bill to.
	* `address_line_1` - (required) Line 1 of the billing street address.
	* `address_line_2` - (optional) Line 2 of the billing street address.
	* `city` - (required) City of the billing address.
	* `state` - (required) State/territory of the billing address.
	* `postal_code` - (required) Postal code of the billing address.
	* `country` - (required) Country of the billing address.
	* `notes` - (optional) Any additional information to record for this address entry.
* `shipping_address` - (optional) The [address](resources/addresses.md) to use for shipping. Only required if `use_billing_address_for_shipping` is `false`.
	* `id` - (optional) The ID of an existing [address](resource/addresses.md). If omitted, a new address will be created.
	* `name` - (required) The name of the person to ship to.
	* `address_line_1` - (required) Line 1 of the shipping street address.
	* `address_line_2` - (optional) Line 2 of the shipping street address.
	* `city` - (required) City of the shipping address.
	* `state` - (required) State/territory of the shipping address.
	* `postal_code` - (required) Postal code of the shipping address.
	* `country` - (required) Country of the shipping address.
	* `notes` - (optional) Any additional information to record for this address entry.
* `use_billing_address_for_shipping` - (optional) Flag that specifies that the billing address should also be used as the shipping address.
* `gift_message` - (optional) Specify a gift message for the order.
* `public_comments` - (optional) Comments that will be displayed to the customer.
* `private_comments` - (optional) Comments that will only be displayed to users with admin and API access.
* `instructions` - (optional) Any additional instructions for this order.
* `payment_method_id` - (optional) The ID of the payment method retrieved from the `GET` request above. Defaults to the ID 0 payment method.
* `credit_card` - (required*) Required if using payment method ID 0 or a gateway, optional for custom methods. Contains the details about the credit card for this order.
	* `number` - (required) The credit card number.
	* `name` - (required) The name on the credit card.
	* `expiration_month` - (required) The month that the credit card expires.
	* `expiration_year` - (required) The year that the credit card expires.
	* `cvv` - (required) The card's security code.
* `customer_payment_method_id` - (optional) The ID of a payment method previously used by the customer.

### Sample request data

```json
{
  "customer": {
    "first_name": "John",
    "last_name": "Doe",
    "email": "jdoe@somebogustestdomainthathopefullydoesntexist.com"
  },
  "billing_address": {
    "name": "John Doe",
    "address_line_1": "123 Test St",
    "city": "Beaumont",
    "state": "TX",
    "postal_code": "77702",
    "country": "US"
  },
  "use_billing_address_for_shipping": true,
  "credit_card": {
    "number": "4111111111111111",
    "name": "John Doe",
    "expiration_month": "12",
    "expiration_year": "2016",
    "cvv": "111"
  }
}
```

### Sample response data

```json
{
  "order_id": 100020,
  "order_approved": true,
  "redirect_url": "OrderView.aspx?orderID=100020&placeorder=yes",
  "message": "Order Successfully Placed. OrderID 100020"
}
```
