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
	"provider_other_charges": null,
	"provider_total_shipping_cost": null,
	"email_sent": false,
	"private_comment": "",
	"shipping_comment": "",
	"created_at": "2014-02-18T13:36:58.357-06:00",
	"updated_at": "2014-02-18T13:36:58.357-06:00",
	"shipping_method_type": "provider",
	"shipment_name": "test1",
	"shipping_provider_name": "UPS"
}
```

Create or Update Shipments
--------------------

To create or update shipments for an order send requests using following endpoint.

```Shell
POST /api/v1/order_shipments
```

Sample Model
------------

```json
{
  "order_id": 100004,
  "shipped_at": "2022-09-06T00:00:00-05:00",
  "tracking_numbers": "123498776",
  "tracking_url": "www.fedex.com/track/123498776",
  "shipping_method": "FedEx Express",
  "shipping_method_id": 1,
  "number_of_packages": 1,
  "total_weight": 2,
  "provider_base_shipping_cost": "",
  "provider_insurance_cost": 0,
  "provider_handling_cost": 0,
  "provider_other_charges": 0,
  "provider_total_shipping_cost": 0,
  "email_sent": false,
  "private_comment": "",
  "shipping_comment": "",
  "shipping_method_type": "provider",
  "shipment_name": "New Shipment",
  "shipping_provider_name": "FedEx",
  "items": [{
      "id": 128,
      "quantity_shipped": 1
  }]
}
```

### Notes
- If you provide a `shipment_name` that matches any existing shipment for the order, the request will update the existing shipment, else it will create a new shipment record.
	- To ensure, you update an existing shipment record, you can specify existing shipment using `id` field. This will update an existing shipment record.

- For nested `items` resource, `id` field is used for providing _OrderItemID_, **not** the _ProductID_

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
            "item_name": "Claymore",
	    "item_nr": "test1"
        },
	...
    ],
    ...
}

```
