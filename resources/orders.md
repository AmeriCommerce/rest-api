orders
======

```shell
GET /api/v1/orders
```

Sample Model
------------

```json
{
	"id": 100000,
	"customer_id": 1,
	"customer_type_id": 0,
	"adcode": "",
	"ordered_at": "2013-11-29T17:12:00-06:00",
	"order_status_id": 5,
	"special_instructions": "",
	"subtotal": 2295,
	"tax_total": 191.4,
	"shipping_total": 25,
	"discount_total": 0,
	"grand_total": 2511.4,
	"cost_total": 0,
	"ip_address": "127.0.0.1",
	"referrer": "",
	"order_shipping_address_id": 1,
	"order_billing_address_id": 1,
	"admin_comments": "",
	"source": "[none]",
	"search_phrase": "",
	"is_ppc": false,
	"ppc_keyword": "",
	"affiliate_id": null,
	"store_id": 1,
	"session_id": 363,
	"handling_total": 0,
	"is_payment_order_only": false,
	"additional_fees": 0,
	"adcode_id": 0,
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2013-11-29T17:12:08.16-06:00",
	"is_gift": false,
	"gift_message": "",
	"public_comments": "",
	"instructions": "",
	"source_group": "",
	"from_subscription_id": null,
	"previous_order_status_id": 2,
	"order_status_last_changed_at": "2014-03-19T13:31:47.923-05:00",
	"discounted_shipping_total": 25,
	"order_number": "",
	"coupon_code": "",
	"order_type": "Order",
	"expires_at": null,
	"expires": false,
	"from_quote_id": null,
	"campaign_code": "",
	"reward_points_credited": false
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/orders/{id}/{nested_resource}`.

### items

### payments

### shipments

### custom_fields