custom_shipping_methods
=======================

```shell
GET /api/v1/custom_shipping_methods
```

**Required scope**: `settings`

Sample Model
------------

```json
{
	"id": 1,
	"name": "Test",
	"is_enabled": true,
	"is_default": true,
	"markup_type": "",
	"markup_amount": "",
	"description": "",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"use_base_rate": false,
	"is_calculated_method": false,
    "admin_only": false
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/custom_shipping_methods/{id}/{nested_resource}`.

### rules

```shell
GET /api/v1/custom_shipping_methods?expand=rules
```

```shell
GET /api/v1/custom_shipping_methods/{id}/rules
```

```json
{
	...
	"rules": [
		{
			"id": 5,
            "shipping_method_id": 1,
            "lower_bound": 0.0000,
            "upper_bound": 50.0000,
            "bound_type": "dollars",
            "amount": 6.9500,
            "amount_type": "dollars",
            "modifier_operation": "plus",
            "modifier_amount": 0.0000,
            "modifier_type": "dollars per item",
            "region_id": 11,
            "warehouse_id": 0,
            "updated_at": "2022-04-25T15:24:08.66-05:00",
            "created_at": "2022-04-25T15:24:08.66-05:00",
            "lower_bound_2": 0.0000,
            "upper_bound_2": 0.0000,
            "bound_type_2": "",
            "customer_type_id": 0,
            "match_values_below_lower_bound": false,
            "match_values_above_upper_bound": false,
            "scope": "",
            "item_min_weight": 0.0000,
            "item_max_weight": 0.0000,
            "item_min_length": 0.0000,
            "item_max_length": 0.0000,
            "item_girth_type": "",
            "item_max_girth": 0.0000
		},
		...
	],
	...
}
```