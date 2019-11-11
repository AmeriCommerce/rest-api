price_calculator_rules
========

```shell
GET /api/v1/price_calculator_rules
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
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
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/price_calculator_rules/{id}/{nested_resource}`.

### modifiers

```shell
GET /api/v1/price_calculator_rules?expand=modifiers
```

```shell
GET /api/v1/price_calculator_rules/{id}/modifiers
```

```json
{
	...
	"modifiers": [
		{
			"id": 1,
			"price_calculator_rule_id": 1,
			"action": "Add",
			"value": 5,
			"modifier_type": "PercentMarkup",
			"optional_action": "Add",
			"optional_value": 5,
			"optional_modifier_type": "Dollars",
			"sort_order": 0,
			"updated_at": "2016-01-01T10:00:00.000-00:00",
			"created_at": "2016-01-01T10:00:00.000-00:00",
			"description": "The Modifier"
		},
		...
	],
	...
}
```