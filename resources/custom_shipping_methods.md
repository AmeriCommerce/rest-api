custom_shipping_methods
=======================

```shell
GET /api/v1/custom_shipping_methods
```

Sample Model
------------

```json
{
	"id": 1,
	"name": "Test",
	"is_enabled": true,
	"is_default": true,
	"markup_type": "",
	"markup_amount": "",
	"description": "",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"use_base_rate": false,
	"is_calculated_method": false
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/custom_shipping_methods/{id}/{nested_resource}`.

### rules