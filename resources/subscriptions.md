subscriptions
=============

```shell
GET /api/v1/subscriptions
```

Sample Model
------------

```json
{
	"id": 1,
	"saved_cart_id": 123,
	"customer_id": 1,
	"next_due_at": "2014-06-12T11:53:06.153-06:00",
	"frequency_type": "Months",
	"frequency": 1,
	"drip_series_id": 0,
	"original_order_id": 100003,
	"shipping_method_name": "USPS 2nd Day",
	"updated_at": "2014-05-12T11:53:06.153-06:00",
	"created_at": "2014-05-12T11:53:06.153-06:00",
	"customer_payment_method_id": null,
	"shipping_address_id": 1,
	"billing_address_id": 1,
	"is_enabled": true,
	"latest_renewal_order_id": null,
	"is_renewal_payment_declined": false,
	"renewal_count": 0,
	"one_time_customer_notice": "",
	"customer_notice": ""
}
```