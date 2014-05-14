discount_methods
================

```shell
GET /api/v1/discount_methods
```

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