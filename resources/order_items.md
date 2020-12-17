order_items
===========

```shell
GET /api/v1/order_items
```

**Required scope**: `read_orders`, `orders`

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
	"weight": 25,
	"is_taxable": true,
	"weight_unit": "Lbs",
	"parent_order_item_id": null,
	"is_quantity_bound_to_parent": false,
	"updated_at": "2013-11-04T09:36:05.7-06:00",
	"created_at": "2013-11-04T09:36:04.827-06:00",
	"height": null,
	"length": null,
	"width": null,
	"size_unit": "In",
	"admin_comments": "",
	"do_not_discount": false,
	"line_item_note": "",
	"gift_message": "",
	"delivery_date": null,
	"is_subscription_product": false,
	"warehouse_id": 0,
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
