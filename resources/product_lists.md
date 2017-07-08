product_lists
=============

```shell
GET /api/v1/product_lists
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 1,
	"name": "Stuff"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/product_lists/{id}/{nested_resource}`.

### items

```shell
GET /api/v1/product_lists?expand=items
```

```shell
GET /api/v1/product_lists/{id}/items
```

```json
{
	...
	"items": [
		{
			"id": 1,
			"product_id": 1,
			"sort_order": 0,
			"variant_inventory_id": null
		},
		{
			"id": 2,
			"product_id": 6,
			"sort_order": 0,
			"variant_inventory_id": null
		},
		{
			"id": 3,
			"product_id": 7,
			"sort_order": 0,
			"variant_inventory_id": null
		},
		...
	],
	...
}
```
