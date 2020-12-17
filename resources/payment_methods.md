payment_methods
===============

Only methods with a `payment_type` of `Custom` are writable. System-defined payment methods are read only.

```shell
GET /api/v1/payment_methods
```

**Required scope**: `settings`

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
	"name": "Send Check or Money Order",
	"updated_at": "2014-05-06T12:24:32.753-05:00",
	"created_at": "2014-05-06T12:24:32.753-05:00"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/payment_methods/{id}/{nested_resource}`.

### fields

```shell
GET /api/v1/payment_methods?expand=fields
```

```shell
GET /api/v1/payment_methods/{id}/fields
```

```json
{
	...
	"fields": [
		{
			"id": 17,
			"name": "Purchase order number",
			"length": 0,
			"sort_order": 0,
			"type": "text",
			"is_required": false,
			"is_hidden": false,
			"is_encrypted": false,
			"is_masked": false,
			"updated_at": "2014-05-06T12:24:32.753-05:00",
			"created_at": "2014-05-06T12:24:32.753-05:00"
		},
		{
			"id": 18,
			"name": "Check Number",
			"length": 12,
			"sort_order": 0,
			"type": "text",
			"is_required": true,
			"is_hidden": false,
			"is_encrypted": false,
			"is_masked": false,
			"updated_at": "2014-05-06T12:24:32.753-05:00",
			"created_at": "2014-05-06T12:24:32.753-05:00"
		}
	],
	...
}
```

### stores

```shell
GET /api/v1/payment_methods?expand=stores
```

```shell
GET /api/v1/payment_methods/{id}/stores
```

```json
{
	...
	"stores": [
		{
			"id": 3,
			"store_id": 1,
			"is_enabled": true,
			"updated_at": "2014-05-06T12:24:32.753-05:00",
			"created_at": "2014-05-06T12:24:32.753-05:00"
		},
		{
			"id": 4,
			"store_id": 3,
			"is_enabled": true,
			"updated_at": "2014-05-06T12:24:32.753-05:00",
			"created_at": "2014-05-06T12:24:32.753-05:00"
		}
	],
	...
}
```