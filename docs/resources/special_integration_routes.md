Integration Routes 
=========

(Available in 2020.3+)

In many cases, it may be necessary to add or update particular resources without having access to identifiers within AmeriCommerce. For example, you may need to update a particular customer, but you may not know the ID of that customer. Or you may need to add a product, which requires a product status, but you don't know the ID of a particular product status. Normal resources require these identifiers. To assist in this need, we provide some special integration routes that are designed to be "ID-less". In these cases we will look up the appropriate resource using unique information other than the ID, or we will create a new resource using the information provided. For example, instead of knowing customer ID, you could send customer email and we would attempt to locate a customer matching that email. Or you would send product status of "In Stock" and we would attempt to find a status matching that name, and create a new product status if one was not found.

Integration routes are provided for customers, products, orders, order shipments, and order payments. These integration routes provide an abbreviated data model as compared to the full resources, but provide a great deal of functionality and flexibility. 

Customers
-----------

```shell
POST /api/v1/customers/integration
```

Lookup
------------
The system will try to find a customer using the email address provided.

Sample Model
------------

```json
{
  "email": "john@doe.com",
  "customer_number": "123456",
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "15555555555",
  "alternate_phone_number": "",
  "company": "Test Company",
  "customer_type": "Wholesale",
  "taxable": true,
  "tax_exemption_number": "",
  "tax_rate": null,
  "reward_tier": "",
  "source": "",
  "source_group": "",
  "sales_note": "",
  "adcode": "",
  "comments": "",
  "addresses": [
    {
      "address_line_1": "123 Any Street",
      "address_line_2": "Suite 560",
      "city": "Beaumont",
      "state": "Texas",
      "postal_code": "77701",
      "country": "United States",
      "default_shipping_address": true,
      "address_phone": "",
      "address_company": "",
      "address_alternate_phone": "",
      "address_fax": "",
      "address_comments": "",
      "default_billing_address": true,
      "address_first_name": "",
      "address_last_name": ""
    },
    {
      "address_line_1": "567 Any Street",
      "address_line_2": "",
      "city": "Beaumont",
      "state": "Texas",
      "postal_code": "77702",
      "country": "United States",
      "default_shipping_address": false,
      "address_phone": "",
      "address_company": "",
      "address_alternate_phone": "",
      "address_fax": "",
      "address_comments": "",
      "default_billing_address": false,
      "address_first_name": "",
      "address_last_name": ""
    }
  ],
  "custom_fields": [
    {
      "custom_field_name": "PlanLevel",
      "custom_field_value": "Gold"
    }
  ]
}
```

Products
-----------

```shell
POST /api/v1/products/integration
```

Lookup
------------
The system will try to find a product using item number (and optionally item name, if provided)

Sample Model
------------

```json
{
  "item_number": "123456",
  "gtin": "",
  "manufacturer_name": "",
  "manufacturer_part_number": "",
  "primary_category_name": "DVD Movies",
  "product_status": "In Stock",
  "item_name": "Sample Product",
  "short_description": "",
  "height": 4,
  "length": 5,
  "width": 6,
  "weight": 1,
  "size_unit": "In",
  "weight_unit": "Lbs",
  "cost": 0.25,
  "price": 1,
  "retail": 2,
  "quantity_on_hand": 10,
  "taxable": true,
  "hidden": false,
  "sort_order": 0,
  "warehouse_name": "",
  "non_shipping_item": false,
  "custom_url": "/sample-product",
  "non_inventory": false,
  "discontinued": false,
  "do_not_discount": false,
  "handling_fee": 5,
  "variants": [
    {
      "group_name": "Color",
      "description": "Red",
      "price_adjustment": 0,
      "price_adjustment_type": "",
      "variant_sort_order": 0,
      "item_number_extension": "",
      "variant_hidden": false,
      "default_selection": false
    },
    {
      "group_name": "Color",
      "description": "Blue",
      "price_adjustment": 0,
      "price_adjustment_type": "",
      "variant_sort_order": 0,
      "item_number_extension": "",
      "variant_hidden": false,
      "default_selection": false
    }
  ],
  "categories": [
    {
      "category_name": "DVD Movies",
      "primary": true
    },
    {
      "category_name": "Action",
      "primary": false
    }
  ],
  "pricing": [
    {
      "id": 15,
      "store_name": "MyStore",
      "customer_type": "",
      "start_date": null,
      "end_date": null,
      "starting_quantity": 5,
      "product_price": 4.95,
      "product_cost": 3.33
    }
  ],
  "attributes": [
    {
      "attribute_group_name": "Condition",
      "attribute_name": "New",
      "attribute_value": ""
    },
    {
      "attribute_group_name": "Edition",
      "attribute_name": "Special",
      "attribute_value": ""
    }
  ],
  "pictures": [
    {
      "image_file": "/shared/images/product/sampleproduct/cover.png",
      "alt_text": "Cover Image",
      "description": "",
      "primary_picture": true,
      "picture_hidden": false,
      "thumbnail_file": ""
    }
  ],
  "custom_fields": [
    {
      "custom_field_name": "Field",
      "custom_field_value": "Value"
    }
  ]
}
```

Orders
-----------

```shell
POST /api/v1/orders/integration
```

Lookup
------------
The system will try to find an order first using order number. If none is found, it will try to find an order using a combination of customer email and order date. If none is found it will create a new order. If more than one is found it will return an error message.

Sample Model
------------

```json
{  
  "order_number": "",
  "customer_email": "john@doe.com",
  "customer_first_name": "John",
  "customer_last_name": "Doe",
  "customer_phone": "1234567890",
  "customer_type": "Wholesale",
  "adcode": "",
  "ordered_at": "2020-06-06T14:23:12-05:00",
  "order_status": "Shipped",
  "subtotal": 9.95,
  "tax_total": 299.75,
  "shipping_total": 50,
  "discount_total": 0,
  "handling_total": 0,
  "additional_fees": 0,
  "grand_total": 359.7,
  "cost_total": 0,
  "selected_shipping_method": "UPS Ground",
  "exported_to_accounting_system": false,
  "referrer": "",
  "shipping_address_line_1": "123 Any St",
  "shipping_address_line_2": "",
  "shipping_address_city": "Beaumont",
  "shipping_address_state": "Texas",
  "shipping_address_postal_code": "77701",
  "shipping_address_company": "",
  "shipping_address_phone": "",
  "shipping_address_first_name": "John",
  "shipping_address_last_name": "Doe",
  "shipping_address_alt_phone": "",
  "shipping_address_country": "United States",
  "billing_address_line_1": "456 Any St",
  "billing_address_line_2": "",
  "billing_address_city": "Beaumont",
  "billing_address_state": "Texas",
  "billing_address_postal_code": "77701",
  "billing_address_company": "",
  "billing_address_phone": "1234567890",
  "billing_address_first_name": "John",
  "billing_address_last_name": "Doe",
  "billing_address_alt_phone": "",
  "billing_address_country": "United States",
  "admin_comments": "",
  "public_comments": "",
  "is_gift": false,
  "gift_message": "",
  "source": "Google",
  "search_phrase": "",
  "source_group": "Organic",
  "coupon_code": "",
  "manufacturer_invoice_number": "123456",
  "manufacturer_invoice_amount": 122,
  "manufacturer_invoice_paid": true,
  "items": [
    {
      "item_number": "MyProductSku",
      "item_name": "My Cool Product",
      "price": 9.95,
      "cost": 0,
      "quantity": 1,
      "weight": 1,
      "is_taxable": true,
      "weight_unit": "Lbs",
      "warehouse_name": "Default",
      "height": 0,
      "length": 0,
      "width": 0,
      "size_unit": "In",
      "tax_code": "",
      "do_not_discount": false,
      "item_gift_message": "",
      "item_description": "",
      "is_non_shipping_item": false
    },
    {
      "item_number": "STEELM-NX5",
      "item_name": "",
      "price": 9.95,
      "cost": 0,
      "quantity": 1,
      "weight": 1,
      "is_taxable": true,
      "weight_unit": "Lbs",
      "warehouse_name": "Default",
      "height": 0,
      "length": 0,
      "width": 0,
      "size_unit": "In",
      "tax_code": "",
      "do_not_discount": false,
      "item_gift_message": "",
      "item_description": "",
      "is_non_shipping_item": false
    }
  ],
  "payments": [
    {
      "order_payment_id": 231,
      "payment_method_name": "Credit Card",
      "payment_type": "CreditCard",
      "is_approved": false,
      "is_declined": false,
      "card_type": "Visa",
      "card_expiration_month": 12,
      "card_expiration_year": 2030,
      "cardholder_name": "John Doe",
      "paid_at": "2020-05-29T07:35:43",
      "approved_at": "2020-05-29T08:35:00",
      "authorization_code": "123456",
      "reject_reason": "",
      "avs_code": "S",
      "transaction_type": "Auth",
      "amount": 359.7,
      "payment_note": "note",
      "is_captured": true,
      "transaction_id": "0987654321",
      "last_four": "1111",
      "is_void": false,
      "gateway_response_code": "S",
      "cvv_response_code": "N",
      "payment_ref_num": "554466"
    }
  ],
  "shipments": [
    {
      "shipped_at": "2020-05-29T10:00:11-05:00",
      "tracking_numbers": "77558844499",
      "tracking_url": "https://www.google.com/tracking",
      "shipping_method": "USPS Media Mail",
      "number_of_packages": 3,
      "total_weight": 34.5,
      "email_sent": false,
      "private_comment": "private 2",
      "shipping_comment": "shipping",
      "shipment_name": "1"
    }
  ],
  "custom_fields": [
    {
      "custom_field_name": "OrderField",
      "custom_field_value": "some value"
    }
  ]
}
```

Order Payments
-----------

```shell
POST /api/v1/order_payments/integration
```

Lookup
------------
The system will first try to find a matching order using the same approach as that described for the `/api/v1/orders/integration` route. If a matching order is found, it will search payments for that order using Order Payment Id, Payment Ref Number, and then Transaction ID to find a match. If none is found, a new payment will be added to the order. If no matching order is found, it will search payments across all orders to try to find a matching payment using Order Payment Id, Payment Ref Number, and then Transaction ID. If still no match is found it will attempt to find a match based on additional payment fields. In the event that still no match is found, or if more than one potential match is found, it will error because it cannot determine which payment to update.

This route is useful if you need to update or add an order payment but don’t have immediate access to all the other information about the order.

Sample Model
------------

```json
{
  "order_payment_id": 212,
  "payment_method_name": "Credit Card",
  "payment_type": "CreditCard",
  "is_approved": false,
  "is_declined": false,
  "card_type": "Visa",
  "card_expiration_month": 12,
  "card_expiration_year": 2030,
  "cardholder_name": "John Doe",
  "paid_at": "2020-05-29T07:35:43",
  "approved_at": "2020-05-29T08:35:00",
  "authorization_code": "123456",
  "reject_reason": "",
  "avs_code": "S",
  "transaction_type": "Auth",
  "amount": 359.7,
  "payment_note": "",
  "is_captured": true,
  "transaction_id": "0987654321",
  "last_four": "1111",
  "is_void": false,
  "gateway_response_code": "S",
  "cvv_response_code": "N",
  "payment_ref_num": "554466",
  "order_id": 100123,
  "order_number": "",
  "customer_email": "john@doe.com",
  "ordered_at": "2020-05-27T14:19:09-05:00"
}
```

Order Shipments
-----------

```shell
POST /api/v1/order_shipments/integration
```

Lookup
------------
The system will first try to find a matching order using the same approach as that described for the `/api/v1/orders/integration` route. If a matching order is found, it will search all shipments for that order for a matching shipment using Tracking Numbers, Shipment name, and then Shipping Method and Date. If no match is found, it will add a new shipment. If no matching order is found, it will search shipments across all orders to try to find a matching shipment. If still no match is found or if more than one potential match is found, it will error because it cannot determine which shipment to update.

You may also optionally specify an order status to apply to the matching order, assuming a match is found.

This route is useful if you need to update or add an order shipment but don’t have immediate access to all the other information about the order.

Sample Model
------------

```json
{
  "shipped_at": "2020-05-29T10:00:11-05:00",
  "tracking_numbers": "77558844499",
  "tracking_url": "https://www.google.com/tracking",
  "shipping_method": "USPS Media Mail",
  "number_of_packages": 3,
  "total_weight": 34.5,
  "email_sent": false,
  "private_comment": "",
  "shipping_comment": "",
  "shipment_name": "First Shipment",
  "order_shipment_id": null,
  "order_id": null,
  "order_number": "5554545457",
  "customer_email": "john@doe.com",
  "ordered_at": "2020-05-27T14:19:09-05:00",
  "order_status": "Shipped"
}
```
