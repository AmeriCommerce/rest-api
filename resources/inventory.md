inventory
=========

`/api/v1/inventory` is a specialized endpoint that is designed to work specifically with product and variant inventory.

## Get Current Inventory

Fetches the current quantity in stock for an existing product. This endpoint expects one of the following pieces of identifying information as a query string parameter:

* `product_id`
* `variant_inventory_id`
* `item_number`
* `gtin`
* `item_name`

###### Example Requests

```shell
GET /api/v1/inventory?product_id=62
```

```shell
GET /api/v1/inventory?variant_inventory_id=12
```

```shell
GET /api/v1/inventory?item_number=60PY2DR
```

###### Example Response

```json
{
	"product_id": 62,
	"variant_inventory_id": null,
	"item_number": "60PY2DR",
	"item_name": "60PY2DR",
	"gtin": "",
	"quantity": 20
}
```

## Adding Inventory

Adds the specified quantity to the quantity in stock. At least one of the following identifiers must be specified:

* `product_id`
* `variant_inventory_id`
* `item_number`
* `gtin`
* `item_name`

###### Example Request

```shell
POST /api/v1/inventory/add
```

```json
{
	"product_id": 62,
	"quantity": 3
}
```

###### Example Response

```json
{
	"product_id": 62,
	"variant_inventory_id": null,
	"item_number": "60PY2DR",
	"item_name": "60PY2DR",
	"gtin": "",
	"quantity": 23
}
```

## Removing Inventory

Removes the specified quantity from the quantity in stock. At least one of the following identifiers must be specified:

* `product_id`
* `variant_inventory_id`
* `item_number`
* `gtin`
* `item_name`

###### Example Request

```shell
POST /api/v1/inventory/remove
```

```json
{
	"product_id": 62,
	"quantity": 3
}
```

###### Example Response

```json
{
	"product_id": 62,
	"variant_inventory_id": null,
	"item_number": "60PY2DR",
	"item_name": "60PY2DR",
	"gtin": "",
	"quantity": 17
}
```

## Setting a Specific Inventory Count

Sets the quantity in stock to the specified quantity. At least one of the following identifiers must be specified:

* `product_id`
* `variant_inventory_id`
* `item_number`
* `gtin`
* `item_name`

###### Example Request

```shell
POST /api/v1/inventory/set
```

```json
{
	"product_id": 62,
	"quantity": 10
}
```

###### Example Response

```json
{
	"product_id": 62,
	"variant_inventory_id": null,
	"item_number": "60PY2DR",
	"item_name": "60PY2DR",
	"gtin": "",
	"quantity": 10
}
```

## Getting Inventory Settings

Pulls the inventory settings for the current store.

###### Example Request

```shell
GET /api/v1/inventory/settings
```

###### Example Response

```json
{
	"track_inventory": true,
	"remove_from_inventory_when": "Ordered",
	"out_of_stock_product_status_id": 2,
	"in_stock_product_status_id": 1,
	"back_order_product_status_id": 3,
	"discontinued_product_status_id": 4,
	"product_hide_no_inventory": false
}
```

## Changing Inventory Settings

Modifies the inventory settings for the current store.

###### Example Request

```shell
PUT /api/v1/inventory/settings
```

```json
{
	"track_inventory": false,
	"remove_from_inventory_when": "Shipped",
	"out_of_stock_product_status_id": 2,
	"in_stock_product_status_id": 1,
	"back_order_product_status_id": 3,
	"discontinued_product_status_id": 4,
	"product_hide_no_inventory": false
}
```

###### Example Response

```json
{
	"track_inventory": false,
	"remove_from_inventory_when": "Shipped",
	"out_of_stock_product_status_id": 2,
	"in_stock_product_status_id": 1,
	"back_order_product_status_id": 3,
	"discontinued_product_status_id": 4,
	"product_hide_no_inventory": false
}
```