order_shipments
===============

```shell
GET /api/v1/order_shipments
```

**Required scope**: `read_orders`, `orders`

Sample Model
------------

```json
{
	"id": 1,
	"order_id": 100013,
	"shipped_at": "2014-02-18T00:00:00-06:00",
	"tracking_numbers": "",
	"tracking_url": "",
	"shipping_method": "UPS 2nd Day Air",
	"shipping_method_id": 3,
	"number_of_packages": null,
	"total_weight": null,
	"provider_base_shipping_cost": "",
	"provider_insurance_cost": null,
	"provider_handling_cost": null,
	"provider_total_shipping_cost": null,
	"email_sent": false,
	"private_comment": "",
	"shipping_comment": "",
	"created_at": "2014-02-18T13:36:58.357-06:00",
	"updated_at": "2014-02-18T13:36:58.357-06:00",
	"shipping_method_type": "custom",
	"shipment_name": "test1"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/order_shipments/{id}/{nested_resource}`.

### items

```shell
GET /api/v1/order_shipments?expand=items
```

```shell
GET /api/v1/order_shipments/{id}/items
```

```json
{
    ...
    "items": [
        {
            "id": 206,
            "quantity_shipped": 1,
            "product_id": 36,
            "item_name": "Claymore"
        },
	...
    ],
    ...
}

```
