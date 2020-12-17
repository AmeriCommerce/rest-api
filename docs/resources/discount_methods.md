discount_methods
================

```shell
GET /api/v1/discount_methods
```

**Required scope**: `read_marketing`, `marketing`

Sample Model
------------

```json
{
	"id": 1,
	"name": "Free Shipping",
	"is_enabled": false,
	"is_strict": true,
	"modifier_operation": "subtract",
	"modifier_amount": "100",
	"modifier_type": "percent",
	"modifier_target": "shipping",
	"use_once": false,
	"expires": false,
	"expires_at": "",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"starts_at": "",
	"remaining_uses": null,
	"notes": "",
	"is_free_shipping_discount": false
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/discount_methods/{id}/{nested_resource}`.

### rules

```shell
GET /api/v1/discount_methods?expand=rules
```

```shell
GET /api/v1/discount_methods/{id}/rules
```

```json
{
	...
	"rules": [
		{
			"id": 1,
			"type": "region",
			"target": "0",
			"updated_at": "2014-03-19T13:31:47.923-05:00",
			"created_at": "2014-03-19T13:31:47.923-05:00",
			"operator_type": "equal to",
			"target_quantity": 1,
			"target_quantity_type": ""
		},
		{
			"id": 2,
			"type": "total dollars",
			"target": "50",
			"updated_at": "2014-03-19T13:31:47.923-05:00",
			"created_at": "2014-03-19T13:31:47.923-05:00",
			"operator_type": "greater than",
			"target_quantity": 1,
			"target_quantity_type": ""
		}
	],
	...
}
```