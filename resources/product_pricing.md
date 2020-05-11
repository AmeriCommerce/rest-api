product_pricing
=============

```shell
GET /api/v1/product_pricing
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 1,
	"product_id": 55,
	"store_id": 60,
	"customer_type_id": 40,
	"variant_inventory_id": 10,
	"sale_type_id": 2,
	"start_date": 2014-03-19T13:31:47.923-05:00,
	"end_date": 2014-03-30T13:31:47.923-05:00,
	"starting_quantity": 60,
	"price": 100.0000,
	"cost": 25.0000,
	"updated_at": 2014-03-19T13:31:47.923-05:00,
	"created_at": 2014-03-19T13:31:47.923-05:00,
	"price_calculation_id": 3,
	"variant_id": 2,
	"variant_price_surcharge":"+ percent"
}
```