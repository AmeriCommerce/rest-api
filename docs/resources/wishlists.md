wishlists
=====

```shell
GET /api/v1/wishlists
```

**Required scope**: `read_orders`, `orders`

Sample Model
------------

```json
{
	"id": 68,
	"name": "",
	"cart_type": "SavedWishList",
	"customer_id": null,
	"is_public": false,
	"updated_at": "2014-04-07T11:55:56.31-05:00",
	"created_at": "2014-04-07T11:44:41.79-05:00",
	"store_id": 1,
	"session_id": 812,
	"discount_total": 0,
	"subtotal": 0,
	"shipping_total": 0,
	"handling_total": 0,
	"tax_total": 0,
	"grand_total": 0,
	"tax_rate": 0,
	"additional_fees": 0,
	"discounted_shipping_total": 0,
	"region_markup_amount": null,
	"non_shipping_discount": 0,
	"gift_certificate_discount": null,
	"coupon_code": "",
	"associated_order_id": null,
	"shipping_estimate_city": null,
        "shipping_estimate_state_code": null,
        "shipping_estimate_postal_code": null,
        "shipping_estimate_country_code": null,
	"is_shipping_billed_to_account": false,
	"customer_payment_method_id": null,
	"payment_method_id": null,
	"is_payment_cart_only": false,
	"lookup_key": null
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/wishlists/{id}/{nested_resource}`.

### items

```shell
GET /api/v1/wishlists?expand=items
```

```shell
GET /api/v1/wishlists/{id}/items
```

```json
{
	...
	"items": [
		{
			"id": 321,
			"product_id": 62,
			"item_number": "60PY2DR",
			"quantity": 2,
			"price": 2295,
			"cost": 0,
			"shipping_address_id": 43,
                        "item_thumbnail": "/shared/images/product/test.jpg",
			"item_url": "",
			"item_name": "60PY2DR",
			"warehouse_id": 0,
			"parent_product_id": null,
			"parent_cart_item_id": null,
			"updated_at": "2014-04-07T11:55:56.31-05:00",
			"created_at": "2014-04-07T11:55:56.31-05:00",
			"cart_id": 68,
			"is_subscription_product": false,
			"configuration": "",
                        "subscription_paused": false,
			"variants": null,
			"personalizations": null
		},
		{
			"id": 298,
			"product_id": 55,
			"item_number": "42LP1",
			"quantity": 1,
			"price": 36.99,
			"cost": 0,
			"shipping_address_id": 43,
                        "item_thumbnail": "/shared/images/product/test2.jpg",
			"item_url": "",
			"item_name": "42LP1",
			"warehouse_id": 0,
			"parent_product_id": null,
			"parent_cart_item_id": null,
			"updated_at": "2014-04-07T11:55:56.31-05:00",
			"created_at": "2014-04-07T11:55:56.31-05:00",
			"cart_id": 68,
			"is_subscription_product": false,
			"configuration": "",
                        "subscription_paused": false,
			"variants": [
				{
					"id": 11,
					"description": "Color: Red",
					"variant_group_id": 3
				}
			],
			"personalizations": [
				{
					"id": 3,
					"answer": "Insert name here"
				}
			]
		},
		...
	],
	...
}
```