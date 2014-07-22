shipping_rate_adjustments
=========================

```shell
GET /api/v1/shipping_rate_adjustments
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 3764,
	"type": "Flat Rate",
	"amount": 15,
	"shipping_method_name": "Priority Shipping",
	"shipping_provider": "Custom",
	"is_unavailable": false,
	"product_id": 9,
	"updated_at": "2014-01-31T15:34:15.363-06:00",
	"created_at": "2014-01-31T15:34:15.363-06:00",
	"available_region_id": 0
}
```