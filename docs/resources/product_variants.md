product_variants
================

```shell
GET /api/v1/product_variants
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 6,
	"product_id": 8,
	"variant_group_id": 4,
	"description": "Blue",
	"price_adjustment": 0,
	"price_adjustment_type": "",
	"sort_order": 0,
	"item_number_extension": "",
	"item_number_sort_order": 0,
	"is_hidden": false,
        "weight": 1.0000,
        "weight_type": "+",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"is_default_selection": false,
        "swatch_file": "",
        "swatch_thumbnail": "",
        "swatch_thumbnail_color": ""
}
```