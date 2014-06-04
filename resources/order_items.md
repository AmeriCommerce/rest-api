order_items
===========

```shell
GET /api/v1/order_items
```

Sample Model
------------

```json
{
	"id": 135,
	"order_id": 100011,
	"product_id": 4,
	"item_number": "glfblls",
	"item_name": "Golf Balls - Titliest",
	"price": 100,
	"cost": 0,
	"quantity": 1,
	"is_discount_item": false,
	"is_taxable": true,
	"parent_order_item_id": null,
	"is_quantity_bound_to_parent": false,
	"updated_at": "2013-11-04T09:36:05.7-06:00",
	"created_at": "2013-11-04T09:36:04.827-06:00",
	"admin_comments": "",
	"do_not_discount": false,
	"line_item_note": "",
	"gift_message": "",
	"delivery_date": null,
	"is_subscription_product": false,
	"description": "test",
	"variants": [
		{
			"id": 7,
			"description": "Color: Blue",
			"variant_group_id": 3
		},
		{
			"id": 23,
			"description": "Special: Normal",
			"variant_group_id": 9
		}
	],
	"personalizations": null
}
```