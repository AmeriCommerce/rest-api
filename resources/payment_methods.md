payment_methods
===============

Only methods with a `payment_type` of `Custom` are writable. System-defined payment methods are read only.

```shell
GET /api/v1/payment_methods
```

Sample Model
------------

```json
{
	"id": 1,
	"payment_type": "Custom",
	"cost_modifier": 0,
	"cost_modifier_type": "Percent",
	"sort_order": 1,
	"is_hidden": false,
	"description": "Shipment will be mailed upon receipt of payment",
	"confirmation_message": "Thank you for your order. Once your check has posted, your shipment will be mailed.",
	"declined_message": "",
	"is_gateway": false,
	"gateway_name": "",
	"updated_at": "2014-05-06T12:24:32.753-05:00",
	"created_at": "2014-05-06T12:24:32.753-05:00"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/payment_methods/{id}/{nested_resource}`.

### fields

### stores