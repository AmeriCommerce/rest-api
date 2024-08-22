customer_payment_methods
========================

```shell
GET /api/v1/customer_payment_methods
```

**Required scope**: `read_people`, `people`

Sample Model
------------

```json
{
	"id": 1,
	"payment_method_id": 0,
	"customer_id": 1,
	"payment_type": "CreditCard",
	"is_default": true,
	"card_id": 1,
	"updated_at": "2014-04-07T11:49:34.09-05:00",
	"created_at": "2014-04-07T11:49:34.09-05:00"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/customer_payment_methods/{id}/{nested_resource}`.

### fields

```shell
GET /api/v1/customer_payment_methods?expand=fields
```

```shell
GET /api/v1/customer_payment_methods/{id}/fields
```

```json
{
	...
	"fields": [
		{
			"id": 53,
			"customer_payment_method_id": 88,
			"type": "text",
			"name": "Sign here",
			"value": "",
			"is_encrypted": false,
			"is_value_masked": false,
			"sort_order": null,
			"updated_at": "2023-05-23T11:23:50.153-05:00",
			"created_at": "2023-05-23T11:23:50.153-05:00"
		},
		...
	],
	...
}
```