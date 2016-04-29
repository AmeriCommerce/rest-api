price_calculator_rule_modifiers
========

```shell
GET /api/v1/price_calculator_rule_modifiers
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
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
}
```