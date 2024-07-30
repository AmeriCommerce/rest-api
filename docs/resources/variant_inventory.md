variant_inventory
=================

```shell
GET /api/v1/variant_inventory
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 1,
	"product_id": 62,
	"inventory": 10,
	"item_number": "VI-ItemTest",
	"manufacturer_item_number": "VI-MfgItemTest",
	"weight": 0,
	"product_status_id": 1,
	"updated_at": "2014-07-21T14:14:44.41-05:00",
	"created_at": "2014-07-21T14:11:39.543-05:00",
	"low_stock_warning_at": null,
	"low_stock_warning_enabled": false,
	"gtin": "",
	"variant_inventory_image": "",
	"height": null,
    "length": null,
    "width": null,
    "retail": null,
    "shipper_hq_shipping_groups": "",
    "shipper_hq_dimensional_rule_groups": "",
    "shipper_hq_packing_boxes": "",
    "description": "Color: VariantTest-Red"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/variant_inventory/{id}/{nested_resource}`.

### pricing

```shell
GET /api/v1/variant_inventory?expand=pricing
```

```shell
GET /api/v1/variant_inventory/{id}/pricing
```

```json
{
	...
	"pricing": [
		{
			"id": 12,
			"store_id": 3,
			"customer_type_id": null,
			"variant_inventory_id": 1,
			"sale_type_id": null,
			"start_date": "2014-07-01T00:00:00-05:00",
			"end_date": "2014-07-31T00:00:00-05:00",
			"starting_quantity": 10,
			"price": 8.99,
			"cost": 5,
			"updated_at": "2014-07-22T13:51:00.99-05:00",
			"created_at": "2014-07-22T13:51:00.99-05:00",
			"price_calculation_id": 1,
			"variant_id": 27,
			"variant_price_surcharge": "+ dollars"
		},
		...
	],
	...
}
```

### variants

```shell
GET /api/v1/variant_inventory?expand=variants
```

```shell
GET /api/v1/variant_inventory/{id}/variants
```

```json
{
	...
	"variants": [
		{
			"id": 26,
			"product_id": 62,
			"variant_group_id": 3,
			"description": "VariantTest-Red",
			"price_adjustment": 5,
			"price_adjustment_type": "+ percent",
			"sort_order": 0,
			"item_number_extension": "vtred",
			"is_hidden": false,
			"updated_at": "2014-07-21T14:10:40.257-05:00",
			"created_at": "2014-07-21T14:10:40.257-05:00",
			"is_default_selection": false,
			"swatch_file": null,
			"swatch_thumbnail": null,
			"swatch_thumbnail_color": null,
			"item_number_sort_order": 1,
			"variant_inventory_id": 1
		},
		...
	],
	...
}
```