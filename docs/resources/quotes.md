quotes
======

```shell
GET /api/v1/quotes
```

**Required scope**: `read_orders`, `orders`

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
	"store_id": 1,
	"session_id": 363,
	"handling_total": 0,
	"is_payment_order_only": false,
	"additional_fees": 0,
	"adcode_id": 0,
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2013-11-29T17:12:08.16-06:00",
	"entered_by": "Admin",
	"is_gift": false,
	"gift_message": "",
	"public_comments": "",
	"instructions": "",
	"source_group": "",
	"previous_order_status_id": 2,
	"order_status_last_changed_at": "2014-03-19T13:31:47.923-05:00",
	"discounted_shipping_total": 25,
	"order_number": null,
	"coupon_code": "",
	"order_type": "Quote",
	"expires_at": null,
	"expires": false,
	"from_quote_id": null,
	"campaign_code": "",
	"reward_points_credited": false,
	"channel": null,
        "device": null,
        "manufacturer_invoice_number": null,
        "manufacturer_invoice_amount": null,
        "manufacturer_invoice_paid": null,
        "sales_agent_user_id": 0,
        "due_date": null,
        "delivery_tax": null,
        "location_id": null,
	"converted_to_order_ids": "101042"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/quotes/{id}/{nested_resource}`.

### items

```shell
GET /api/v1/quotes?expand=items
```

```shell
GET /api/v1/quotes/{id}/items
```

```json
{
	...
	"items": [
		{
			"id": 798,
			"order_id": 100000,
			"product_id": 55,
			"item_number": "42LP1",
			"item_name": "42LP1",
			"price": 36.99,
			"cost": 0,
			"quantity": 1,
			"is_discount_item": false,
			"weight": 25.0000,
			"is_taxable": true,
			"weight_unit": "Lbs",
			"is_non_shipping_item": false,
			"warehouse_id": 0,
			"variant_inventory_id": null,
			"parent_order_item_id": null,
			"is_quantity_bound_to_parent": false,
			"updated_at": "2014-04-07T11:55:56.31-05:00",
			"created_at": "2014-04-07T11:55:56.31-05:00",
			"height": 0.0000,
			"length": 0.0000,
			"width": 0.0000,
			"size_unit": "In",
			"tax_code": "",
			"item_number_full": "HTB-N810DV",
			"admin_comments": "",
			"do_not_discount": false,
			"line_item_note": "",
			"order_shipping_address_id": null,
			"gift_message": "",
			"delivery_date": null,
			"discount_amount": 0.0000,
			"discount_percentage": 0.0000,
			"is_subscription_product": false,
			"description": "",
			"tax": 0.0000,
			"configuration": "",
			"status": "",
			"shipping_classification_code": "",
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

### custom_fields

```shell
GET /api/v1/quotes?expand=custom_fields
```

```shell
GET /api/v1/quotes/{id}/custom_fields
```

```json
{
	...
	"custom_fields": [
		{
			"name": "testme",
			"value": "my value"
		},
		...
	],
	...
}
```