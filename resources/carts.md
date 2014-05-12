carts
=====

```shell
GET /api/v1/carts
```

Sample Model
------------

```json
{
	"id": 68,
	"name": "",
	"cart_type": "NormalCart",
	"customer_id": null,
	"is_public": false,
	"updated_at": "2014-04-07T11:55:56.31-05:00",
	"created_at": "2014-04-07T11:44:41.79-05:00",
	"store_id": 1,
	"session_id": 812,
	"discount_total": 0,
	"subtotal": 4605.99,
	"shipping_total": 25,
	"handling_total": 0,
	"tax_total": 0,
	"grand_total": 4630.99,
	"tax_rate": 0,
	"additional_fees": 0,
	"discounted_shipping_total": 25,
	"region_markup_amount": null,
	"non_shipping_discount": 0,
	"gift_certificate_discount": null,
	"coupon_code": "",
	"associated_order_id": null,
	"is_shipping_billed_to_account": false,
	"customer_payment_method_id": null,
	"payment_method_id": null,
	"is_payment_cart_only": false
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/carts/{id}/{nested_resource}`.

### items