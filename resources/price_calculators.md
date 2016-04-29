price_calculators
========

```shell
GET /api/v1/price_calculators
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id":1,
	"calculation_name":"Tier 1",
	"description":"",
	"updated_at":"2016-01-01T10:00:00.000-00:00",
	"created_at":"2016-01-01T10:00:00.000-00:00",
	"item_numbers_regex":""
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/price_calculators/{id}/{nested_resource}`.

### rules

```shell
GET /api/v1/price_calculators?expand=rules
```

```shell
GET /api/v1/price_calculators/{id}/rules
```

```json
{
	...
	"rules": [
		{
			"id": 1,
			"price_calculator_id": 1,
			"customer_type_id": 1,
			"store_id": 1,
			"starting_quantity": 5,
			"price_base_type": "BaseCostPassedIn",
			"updated_at": "2016-01-01T10:00:00.000-00:00",
			"created_at": "2016-01-01T10:00:00.000-00:00",
			"specific_base_price": 0
		},
		...
	],
	...
}
```