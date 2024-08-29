discount_actions
================

```shell
GET /api/v1/discount_actions
```

**Required scope**: `read_marketing`, `marketing`

Sample Model
------------

```json
{
	"id": 3,
        "discount_method_id": 6,
        "is_exclusive": false,
        "is_strict": false,
        "is_active": true,
        "modifier_operation": "subtract",
        "modifier_amount": "50",
        "modifier_type": "percent",
        "modifier_target": "total",
        "sort_order": 20,
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/discount_actions/{id}/{nested_resource}`.

### rules

```shell
GET /api/v1/discount_actions?expand=rules
```

```shell
GET /api/v1/discount_actions/{id}/rules
```

```json
{
	...
	"rules": [
		{
			"id": 1,
                        "discount_method_id": null,
			"type": "region",
			"target": "0",
			"updated_at": "2014-03-19T13:31:47.923-05:00",
			"created_at": "2014-03-19T13:31:47.923-05:00",
			"operator_type": "equal to",
			"target_quantity": 1,
			"target_quantity_type": "",
                        "discount_action_id": 1,
                        "is_action_rule": true,
                        "bogo_discount_buy_quantity": null,
                        "bogo_discount_quantity": null,
                        "bogo_max_use_per_order": null,
                        "discount_from_high_to_low": false
		},
		...
	],
	...
}
```