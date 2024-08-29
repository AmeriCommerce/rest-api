discount_methods
================

```shell
GET /api/v1/discount_methods
```

**Required scope**: `read_marketing`, `marketing`

Sample Model
------------

```json
{
	"id": 1,
	"name": "Free Shipping",
	"is_enabled": false,
	"is_strict": true,
	"use_once": false,
	"expires": false,
	"expires_at": "",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"starts_at": "",
	"remaining_uses": null,
	"notes": "",
	"is_free_shipping_discount": false,
        "is_exclusive": false,
        "uses": 0,
        "exclude_child_items": false,
        "exclude_subscription_renew": false,
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/discount_methods/{id}/{nested_resource}`.

### rules

```shell
GET /api/v1/discount_methods?expand=rules
```

```shell
GET /api/v1/discount_methods/{id}/rules
```

```json
{
	...
	"rules": [
		{
			"id": 1,
                        "discount_method_id": 1,
			"type": "region",
			"target": "0",
			"updated_at": "2014-03-19T13:31:47.923-05:00",
			"created_at": "2014-03-19T13:31:47.923-05:00",
			"operator_type": "equal to",
			"target_quantity": 1,
			"target_quantity_type": "",
                        "discount_action_id": null,
                        "is_action_rule": false,
                        "bogo_discount_buy_quantity": null,
                        "bogo_discount_quantity": null,
                        "bogo_max_use_per_order": null,
                        "discount_from_high_to_low": false
		},
		{
			"id": 2,
                        "discount_method_id": 1,
			"type": "total dollars",
			"target": "50",
			"updated_at": "2014-03-19T13:31:47.923-05:00",
			"created_at": "2014-03-19T13:31:47.923-05:00",
			"operator_type": "greater than",
			"target_quantity": 1,
			"target_quantity_type": "",
                        "discount_action_id": null,
                        "is_action_rule": false,
                        "bogo_discount_buy_quantity": null,
                        "bogo_discount_quantity": null,
                        "bogo_max_use_per_order": null,
                        "discount_from_high_to_low": false
		}
	],
	...
}
```

### actions

```shell
GET /api/v1/discount_methods?expand=actions
```

```shell
GET /api/v1/discount_methods/{id}/actions
```

```json
{
	...
	"actions": [
		{
			"id": 6,
                        "discount_method_id": 1,
                        "is_exclusive": false,
                        "is_strict": false,
                        "is_active": true,
                        "modifier_operation": "subtract",
                        "modifier_amount": "1",
                        "modifier_type": "dollars",
                        "modifier_target": "matcheditems",
                        "sort_order": 10
		},
		...
	],
	...
}
```