gift_certificates
=================

```shell
GET /api/v1/gift_certificates
```

**Required scope**: `read_marketing`, `marketing`

Sample Model
------------

```json
{
	"id": 1,
	"code": "GC-KDK-44-KGKHBX",
	"original_order_id": null,
	"from_customer_id": null,
	"recipient_email": "test@not-my-real-address.zzz",
	"recipient_name": "Chris Allen",
	"recipient_shipping_address": "",
	"gift_message": "It's dangerous to go alone. Take this.",
	"status": "Active",
	"is_pre_tax_discount": false,
	"gift_certificate_type": "blah",
	"comments": "",
	"created_at": null,
	"expires_at": "2014-12-31T00:00:00-06:00",
	"store_id": 3,
	"current_amount": 100,
	"original_amount": 100,
	"updated_at": "2014-03-12T08:47:54.51-05:00",
	"customer_id": 6,
	"expires": true,
	"order_item_id": null
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/gift_certificates/{id}/{nested_resource}`.

### transactions

```shell
GET /api/v1/gift_certificates?expand=transactions
```

```shell
GET /api/v1/gift_certificates/{id}/transactions
```

```json
{
	...
	"transactions": [
		{
			"id": 1,
                        "gift_certificate_id": 1,
			"action": "Create",
			"amount": 100,
			"is_pre_tax_discount": false,
			"order_id": 0,
			"order_payment_id": null,
			"updated_at": "2014-03-12T08:47:54.44-05:00",
			"created_at": "2014-03-12T08:47:54.44-05:00",
			"status": "Approved"
		},
		{
			"id": 2,
                        "gift_certificate_id": 1,
			"action": "SetActive",
			"amount": 0,
			"is_pre_tax_discount": false,
			"order_id": 0,
			"order_payment_id": null,
			"updated_at": "2014-03-12T08:47:54.533-05:00",
			"created_at": "2014-03-12T08:47:54.533-05:00",
			"status": "Approved"
		}
	]
	...
}
```