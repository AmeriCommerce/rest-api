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