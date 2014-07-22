discount_rules
==============

```shell
GET /api/v1/discount_rules
```

**Required scope**: `read_marketing`, `marketing`

Sample Model
------------

```json
{
	"id": 3,
	"discount_method_id": 5,
	"type": "an item in cart (multiplied)",
	"target": "glfblls",
	"updated_at": "2013-10-07T14:45:24.64-05:00",
	"created_at": "2013-10-07T14:44:57.373-05:00",
	"operator_type": "contains",
	"target_quantity": 1,
	"target_quantity_type": "MinimumOf"
}
```