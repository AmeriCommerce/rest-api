customer_types
==============

```shell
GET /api/v1/customer_types
```

**Required scope**: `read_people`, `people`

Sample Model
------------

```json
{
	"id": 1,
	"name": "Wholesale",
	"customer_level": 1,
	"description": "",
	"updated_at": "2004-10-08T00:00:00-05:00",
	"created_at": "2004-10-08T00:00:00-05:00"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/customer_types/{id}/{nested_resource}`.

### customer_type_payment_methods_availability

```shell
GET /api/v1/customer_types?expand=customer_type_payment_methods_availability
```

```shell
GET /api/v1/customer_types/{id}/customer_type_payment_methods_availability
```

```json
{
	...
	"customer_type_payment_methods_availability": [
		{
			"id": 1,
            "payment_method_id": 6,
            "status": "Active",
            "customer_type_id": 13
		},
		...
	],
	...
}
```