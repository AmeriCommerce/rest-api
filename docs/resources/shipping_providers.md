shipping_providers
==================

```shell
GET /api/v1/shipping_providers
```

**Required scope**: `settings`

Sample Model
------------

```json
{
	"id": 1,
	"name": "UPS",
	"provider_code": "UPS",
	"is_enabled": true,
	"markup_amount": "0",
	"markup_type": "%",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"additional_markup_percent": 0,
	"additional_weight_per_package": 0
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/shipping_providers/{id}/{nested_resource}`.

### services

```shell
GET /api/v1/shipping_providers?expand=services
```

```shell
GET /api/v1/shipping_providers/{id}/services
```

```json
{
	...
	"services": [
		{
			"id": 1,
            "is_enabled": true,
            "shipping_provider_id": 1,
            "identifier": "UPS Ground",
            "name": "DHL Ground",
            "shipping_provider_code": "",
            "updated_at": null,
            "created_at": null,
            "allow_apo": false,
            "allow_po_box": false
		},
		...
	],
	...
}
```