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
        "last_four": "",
	"is_void": false,
	"gateway_response_code": "",
	"cvv_response_code": "",
        "payment_ref_num": "",
        "store_method_payment_id": 0
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/order_payments/{id}/{nested_resource}`.

### fields

```shell
GET /api/v1/order_payments?expand=fields
```

```shell
GET /api/v1/order_payments/{id}/fields
```

```json
{
    ...
    "fields": [
        {
            "id": 14,
            "order_payment_id": 95,
            "name": "Sign your name",
            "type": "text",
            "value": "",
            "is_encrypted": false,
            "is_masked": false,
            "updated_at": "2023-05-15T12:59:19.14-05:00",
            "created_at": "2023-05-15T12:59:19.14-05:00"
        },
	...
    ],
    ...
}

```