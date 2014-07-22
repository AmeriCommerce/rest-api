order_payments
==============

```shell
GET /api/v1/order_payments
```

**Required scope**: `read_orders`, `orders`

Sample Model
------------

```json
{
	"id": 1,
	"customer_id": 1,
	"order_id": 100000,
	"customer_payment_method_id": 1,
	"payment_method_id": 0,
	"payment_type": "CreditCard",
	"is_approved": false,
	"is_declined": false,
	"card_type": "Visa",
	"card_expiration_month": 12,
	"card_expiration_year": 2015,
	"cardholder_name": "John Doe",
	"paid_at": "2014-04-07T11:43:09.103-05:00",
	"approved_at": "",
	"authorization_code": "",
	"reject_reason": "",
	"avs_code": "",
	"payment_method_name": "Credit Card",
	"transaction_type": "None",
	"amount": 60.73,
	"payment_note": "",
	"updated_at": "2014-04-07T11:43:09.127-05:00",
	"created_at": "2014-04-07T11:43:09.127-05:00",
	"gift_certificate_id": null,
	"is_captured": false,
	"transaction_id": "",
	"is_void": false,
	"gateway_response_code": "",
	"cvv_response_code": ""
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/order_payments/{id}/{nested_resource}`.

### fields