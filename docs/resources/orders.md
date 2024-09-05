orders
======

```shell
GET /api/v1/orders
```

**Required scope**: `read_orders`, `orders`

Sample Model
------------

```json
{
	"id": 100000,
	"customer_id": 1,
	"customer_type_id": 0,
	"adcode": "",
	"ordered_at": "2013-11-29T17:12:00-06:00",
	"order_status_id": 5,
	"special_instructions": "",
	"subtotal": 2295,
	"tax_total": 191.4,
	"shipping_total": 25,
	"discount_total": 0,
	"grand_total": 2511.4,
	"cost_total": 0,
	"selected_shipping_method": "FedEx Express Saver",
	"ip_address": "127.0.0.1",
        "exported_to_accounting_system": 0,
	"referrer": "",
	"order_shipping_address_id": 1,
	"order_billing_address_id": 1,
	"admin_comments": "",
	"source": "[none]",
	"search_phrase": "",
	"is_ppc": false,
	"ppc_keyword": "",
	"store_id": 1,
	"session_id": 363,
	"handling_total": 0,
	"is_payment_order_only": false,
	"selected_shipping_provider_service": "FEDEX_EXPRESS_SAVER",
	"additional_fees": 0,
	"adcode_id": 0,
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2013-11-29T17:12:08.16-06:00",
        "entered_by": "test@test.com",
	"is_gift": false,
	"gift_message": "",
	"public_comments": "",
	"instructions": "",
	"source_group": "",
	"from_subscription_id": null,
	"previous_order_status_id": 2,
	"order_status_last_changed_at": "2014-03-19T13:31:47.923-05:00",
	"discounted_shipping_total": 25,
	"order_number": "",
	"coupon_code": "",
	"order_type": "Order",
	"expires_at": null,
	"expires": false,
	"from_quote_id": null,
	"campaign_code": "",
	"reward_points_credited": false,
        "channel": "Online",
        "device": "None",
        "manufacturer_invoice_number": "",
        "manufacturer_invoice_amount": 0.0000,
        "manufacturer_invoice_paid": false,
        "sales_agent_user_id": 0,
        "due_date": null,
        "delivery_tax": 0.0000,
        "location_id": null,
        "shipping_selections": [
                {
                    "classification_code": "",
                    "shipping_provider": "FedEx",
                    "shipping_method": "FedEx Express Saver"
                }
        ],
       "entered_by_type": "Customer"
}
```

Status Change Events
--------------------

To update the status of an order and trigger order-status-changed events such as sending notification emails to customers, a special endpoint must be used.

###### Example Request

```Shell
PUT /api/v1/orders/{order_id}/status
```

```json
{
"order_status_id": 3
}
```

Process Payment
--------------------

To add a card payment, a special endpoint must be used. If amount is left blank, the order total will be used as amount. 

###### Example Request

```Shell
POST /api/v1/orders/{order_id}/process_payment
```

```json
{
    "card_id": 41,
    "customer_id": 6,
    "amount": 12.43
    "cvv": ""
}
```

###### Example Response

```json
{
    "payment_declined": false,
    "response": "",
    "payment_processed": false
}
```

Process Payments Payment Order
--------------------

To process payments on a payment order, a special endpoint must be used.

###### Example Request

```Shell
POST /api/v1/orders/{order_id}/process_payments
```

```json
{
    "force_process_all": false
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/orders/{id}/{nested_resource}`.

### items

```shell
GET /api/v1/orders?expand=items
```

```shell
GET /api/v1/orders/{id}/items
```

```json
{
	...
	"items": [
		{
			"id": 135,
	                "order_id": 100000,
	                "product_id": 4,
	                "item_number": "glfblls",
	                "item_name": "Golf Balls - Titliest",
	                "price": 100,
	                "cost": 0,
	                "quantity": 1,
	                "is_discount_item": false,
	                "weight": 25,
	                "is_taxable": true,
	                "weight_unit": "Lbs",
                        "is_non_shipping_item": false,
                        "variant_inventory_id": null,
	                "parent_order_item_id": null,
	                "is_quantity_bound_to_parent": false,
	                "updated_at": "2013-11-04T09:36:05.7-06:00",
	                "created_at": "2013-11-04T09:36:04.827-06:00",
	                "height": null,
	                "length": null,
	                "width": null,
	                "size_unit": "In",
                        "tax_code": "",
                        "item_number_full": "glfblls",
	                "admin_comments": "",
	                "do_not_discount": false,
	                "line_item_note": "",
                        "order_shipping_address_id": null,
	                "gift_message": "",
	                "delivery_date": null,
                        "discount_amount": 0.0000,
                        "discount_percentage": 0.0000,
	                "is_subscription_product": false,
	                "warehouse_id": 0,
	                "description": "test",
                        "tax": 5.5275,
                        "configuration": "",
                        "status": "",
                        "shipping_classification_code": "tx",
	                "variants": [
		                {
			                "id": 7,
			                "description": "Color: Blue",
			                "variant_group_id": 3
		                },
		                {
			                "id": 23,
			                "description": "Special: Normal",
			                "variant_group_id": 9
		                }
	                ],
	                "personalizations": null
		},
		...
	],
	...
}
```

### payments

```shell
GET /api/v1/orders?expand=payments
```

```shell
GET /api/v1/orders/{id}/payments
```

```json
{
	...
	"payments": [
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
		},
		...
	],
	...
}
```

### shipments

```shell
GET /api/v1/orders?expand=shipments
```

```shell
GET /api/v1/orders/{id}/shipments
```

```json
{
	...
	"shipments": [
		{
			"id": 2,
                        "order_id": 100000,
                        "shipped_at": "2023-06-09T00:00:00-05:00",
                        "tracking_numbers": "",
                        "tracking_url": "",
                        "shipping_method": "FedEx Express Saver",
                        "shipping_method_id": 30,
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
                        "created_at": "2023-06-09T08:37:40.033-05:00",
                        "updated_at": "2023-06-16T08:32:30.353-05:00",
                        "shipping_method_type": "provider",
                        "shipment_name": "1",
                        "shipping_provider_name": "FedEx"
		},
		...
	],
	...
}
```

### custom_fields

```shell
GET /api/v1/orders?expand=custom_fields
```

```shell
GET /api/v1/orders/{id}/custom_fields
```

```json
{
	...
	"custom_fields": [
		{
			"name": "testme",
			"value": "my value"
		},
		...
	],
	...
}
```