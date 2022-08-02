subscriptions
=============

```shell
GET /api/v1/subscriptions
```

**Required scope**: `read_orders`, `orders`

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

Nested Resources
----------------

Accessible via the `?includelookups=1` parameter.


```shell
GET /api/v1/subscriptions?includelookups=1
```
```json
{
	...
	{
    "total_count": 1,
    "subscriptions": [
        {
            "id": 13,
            "saved_cart_id": 3844,
            "customer_id": 105,
            "next_due_at": "2021-08-04T15:20:35-05:00",
            "frequency_type": "Days",
            "frequency": 0,
            "drip_series_id": 2,
            "original_order_id": 100243,
            "shipping_method_name": "FedEx Home Delivery",
            "updated_at": "2022-01-19T10:23:53.167-06:00",
            "created_at": "2021-08-04T15:20:39.997-05:00",
            "customer_payment_method_id": null,
            "shipping_address_id": null,
            "billing_address_id": null,
            "is_enabled": false,
            "latest_renewal_order_id": null,
            "is_renewal_payment_declined": false,
            "renewal_count": 0,
            "one_time_customer_notice": "",
            "customer_notice": "",
            "cart_info": {
                "id": 3844,
                "name": "Subscription for Order: 100243",
                "cart_type": "SavedCart",
                "customer_id": 105,
                "is_public": false,
                "updated_at": "2021-08-04T15:20:39.967-05:00",
                "created_at": "2021-08-04T15:20:39.967-05:00",
                "store_id": 19,
                "session_id": 144311,
                "discount_total": 0.0,
                "subtotal": 1886.0000,
                "shipping_total": 0.0,
                "handling_total": 0.0,
                "tax_total": 0.0,
                "grand_total": 1886.0000,
                "tax_rate": 0.0000,
                "additional_fees": 0.0000,
                "discounted_shipping_total": 0.0000,
                "region_markup_amount": null,
                "non_shipping_discount": 0.0000,
                "gift_certificate_discount": null,
                "coupon_code": "",
                "associated_order_id": null,
                "shipping_estimate_city": "",
                "shipping_estimate_state_code": "",
                "shipping_estimate_postal_code": "",
                "shipping_estimate_country_code": "",
                "is_shipping_billed_to_account": false,
                "customer_payment_method_id": null,
                "payment_method_id": null,
                "is_payment_cart_only": false,
                "items": [
                    {
                        "id": 5798,
                        "product_id": 66,
                        "item_number": "BR85",
                        "quantity": 1,
                        "price": 1886.0000,
                        "cost": 450.0000,
                        "shipping_address_id": null,
                        "item_thumbnail": "/Shared/Images/Product/img.png",
                        "item_url": "",
                        "item_name": "Product1",
                        "warehouse_id": 3,
                        "parent_product_id": null,
                        "parent_cart_item_id": null,
                        "updated_at": "2021-08-04T15:20:39.98-05:00",
                        "created_at": "2021-08-04T15:20:39.98-05:00",
                        "cart_id": 3844,
                        "is_subscription_product": false,
                        "vendor_store_id": null,
                        "fitment": "",
                        "configuration": "",
                        "variants": [
                            {
                                "id": 48,
                                "description": null,
                                "variant_group_id": 7
                            }
                        ],
                        "personalizations": null
                    }
                ],
                "lookup_key": "KjvSkStG7tg%3D"
            },
            "customer": {
                "id": 105,
                "customer_number": "",
                "last_name": "Test",
                "first_name": "Ac",
                "email": "test@mail.com",
                "phone_number": "5555555555",
                "registered_at": "2021-06-21T12:21:39-05:00",
                "last_visit_at": "2021-06-21T12:21:39-05:00",
                "adcode": "",
                "adcode_id": 0,
                "affiliate_id": 0,
                "customer_type_id": null,
                "is_no_tax_customer": false,
                "comments": "",
                "store_id": 19,
                "source": "",
                "search_string": "",
                "no_account": true,
                "sales_person": "",
                "alternate_phone_number": "",
                "is_affiliate_customer": false,
                "updated_at": "2021-06-21T12:21:41.393-05:00",
                "created_at": "2021-06-21T10:10:56.127-05:00",
                "username": "",
                "is_contact_information_only": true,
                "tax_exemption_number": "",
                "company": "",
                "source_group": "",
                "sales_person_user_id": null,
                "store_payment_methods_enabled": [],
                "tax_rate": null,
                "reward_tier_id": null,
                "sub": ""
            }
        }
    ]
}
		...
	],
	...
}
```