Resource List
=============

All API URLs start with `https://[mystorename.com]/api/v1/`, where `[mystorename.com]` is the SSL domain name of your AmeriCommerce. See [Common Usage](https://github.com/AmeriCommerce/rest-api/blob/master/common_usage.md) for a more detailed explanation of most of the operations these provide.

### People

| Name | Collections |
| ---- | ----------- |
| [addresses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/addresses.md) |
| [customers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/customers.md) | addresses, reward\_points, custom\_fields |
| [customer_types](https://github.com/AmeriCommerce/rest-api/blob/master/resources/customer_types.md) | |
| [customer_payment_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/customer_payment_methods.md) | fields |
| [profiles](https://github.com/AmeriCommerce/rest-api/blob/master/resources/profiles.md) | contacts |
| [users](https://github.com/AmeriCommerce/rest-api/blob/master/resources/users.md) | |

### Orders

| Name | Collections |
| ---- | ----------- |
| [carts](https://github.com/AmeriCommerce/rest-api/blob/master/resources/carts.md) | items |
| [cart_items](https://github.com/AmeriCommerce/rest-api/blob/master/resources/cart_items.md) | child_items |
| [credit_cards](https://github.com/AmeriCommerce/rest-api/blob/master/resources/credit_cards.md) | |
| [orders](https://github.com/AmeriCommerce/rest-api/blob/master/resources/orders.md) | items, payments, shipments, custom_fields |
| [order_addresses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_addresses.md) | |
| [order_items](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_items.md) | |
| [order_payments](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_payments.md) | fields |
| [order_shipments](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_shipments.md) | items |
| [order_statuses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_statuses.md) | |
| [quotes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/quotes.md) | items, payments, shipments, custom_fields |
| [subscriptions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/subscriptions.md) | |
| [wishlists](https://github.com/AmeriCommerce/rest-api/blob/master/resources/wishlists.md) | items |

### Catalog

| Name | Collections |
| ---- | ----------- |
| [attributes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/attributes.md) | |
| [attribute_groups](https://github.com/AmeriCommerce/rest-api/blob/master/resources/attribute_groups.md) | |
| [categories](https://github.com/AmeriCommerce/rest-api/blob/master/resources/categories.md) | products, custom_fields |
| [inventory](https://github.com/AmeriCommerce/rest-api/blob/master/resources/inventory.md)* | |
| [manufacturers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/manufacturers.md) | |
| [notifications](https://github.com/AmeriCommerce/rest-api/blob/master/resources/notifications.md) | |
| [price_calculators](https://github.com/AmeriCommerce/rest-api/blob/master/resources/price_calculators.md) | rules |
| [price_calculator_rules](https://github.com/AmeriCommerce/rest-api/blob/master/resources/price_calculator_rules.md) | modifiers |
| [price_calculator_rule_modifiers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/price_calculator_rule_modifiers.md) | |
| [products](https://github.com/AmeriCommerce/rest-api/blob/master/resources/products.md) | variants, personalizations, related, categories, pricing, attributes, variant\_inventory, pictures, child\_products, shipping\_rate\_adjustments, reviews, custom\_fields |
| [product_lists](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_lists.md) | |
| [product_pictures](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_pictures.md) | |
| [product_reviews](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_reviews.md) | ratings |
| [product_statuses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_statuses.md) | |
| [product_variants](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_variants.md) | |
| [shipping_rate_adjustments](https://github.com/AmeriCommerce/rest-api/blob/master/resources/shipping_rate_adjustments.md) | |
| [variant_groups](https://github.com/AmeriCommerce/rest-api/blob/master/resources/variant_groups.md) | variants |
| [variant_inventory](https://github.com/AmeriCommerce/rest-api/blob/master/resources/variant_inventory.md) | pricing, variants |

\* Special endpoint

### Content

| Name | Collections |
| ---- | ----------- |
| [blogs](https://github.com/AmeriCommerce/rest-api/blob/master/resources/blogs.md) | categories, posts |
| [blog_categories](https://github.com/AmeriCommerce/rest-api/blob/master/resources/blog_categories.md) | posts |
| [blog_posts]https://github.com/AmeriCommerce/rest-api/blob/master/(resources/blog_posts.md) | categories |
| [links](https://github.com/AmeriCommerce/rest-api/blob/master/resources/links.md) | child_links |
| [pages](https://github.com/AmeriCommerce/rest-api/blob/master/resources/pages.md) | |

### Marketing

| Name | Collections |
| ---- | ----------- |
| [adcodes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/adcodes.md) | |
| [affiliates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/affiliates.md) | |
| [coupon_codes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/coupon_codes.md) | |
| [discount_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/discount_methods.md) | rules |
| [discount_rules](https://github.com/AmeriCommerce/rest-api/blob/master/resources/discount_rules.md) | |
| [drips](https://github.com/AmeriCommerce/rest-api/blob/master/resources/drips.md) | members, events |
| [email_templates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/email_templates.md) | |
| [gift_certificates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/gift_certificates.md) | transactions |
| [gift_certificate_transactions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/gift_certificate_transactions.md) | |
| [mailing_lists](https://github.com/AmeriCommerce/rest-api/blob/master/resources/mailing_lists.md) | members |

### Tools

| Name | Collections |
| ---- | ----------- |
| [custom_fields](https://github.com/AmeriCommerce/rest-api/blob/master/resources/custom_fields.md) | values, list_items, stores |
| [custom\_field\_values](https://github.com/AmeriCommerce/rest-api/blob/master/resources/custom_field_values.md) | |

### Settings

| Name | Collections |
| ---- | ----------- |
| [custom_shipping_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/custom_shipping_methods.md)	| rules |
| [payment_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/payment_methods.md)	| fields, stores |
| [regions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/regions.md)	| |
| [shipping_providers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/shipping_providers.md)	| services |
| [tax_rates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/tax_rates.md)	| |
| [url_redirects](https://github.com/AmeriCommerce/rest-api/blob/master/resources/url_redirects.md)	| |
| [warehouses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/warehouses.md)	| |

### System

| Name | Collections |
| ---- | ----------- |
| [sessions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/sessions.md)	| |
| [stores](https://github.com/AmeriCommerce/rest-api/blob/master/resources/stores.md)	| |
