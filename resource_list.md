Resource List
=============

All API URLs start with `https://[mystorename.com]/api/v1/`, where `[mystorename.com]` is the SSL domain name of your Spark Pay Online Store. See [Common Usage](common_usage.md) for a more detailed explanation of most of the operations these provide.

### People

| Name | Collections |
| ---- | ----------- |
| [addresses](resources/addresses.md) |
| [customers](resources/customers.md) | addresses, reward\_points, custom\_fields |
| [customer_types](resources/customer_types.md) | |
| [customer_payment_methods](resources/customer_payment_methods.md) | fields |
| [profiles](resources/profiles.md) | contacts |
| [users](resources/users.md) | |

### Orders

| Name | Collections |
| ---- | ----------- |
| [carts](resources/carts.md) | items |
| [cart_items](resources/cart_items.md) | child_items |
| [credit_cards](resources/credit_cards.md) | |
| [orders](resources/orders.md) | items, payments, shipments, custom_fields |
| [order_addresses](resources/order_addresses.md) | |
| [order_items](resources/order_items.md) | |
| [order_payments](resources/order_payments.md) | fields |
| [order_shipments](resources/order_shipments.md) | items |
| [order_statuses](resources/order_statuses.md) | |
| [quotes](resources/quotes.md) | items, payments, shipments, custom_fields |
| [subscriptions](resources/subscriptions.md) | |
| [wishlists](resources/wishlists.md) | items |

### Catalog

| Name | Collections |
| ---- | ----------- |
| [attributes](resources/attributes.md) | |
| [attribute_groups](resources/attribute_groups.md) | |
| [categories](resources/categories.md) | products, custom_fields |
| [inventory](resources/inventory.md)* | |
| [manufacturers](resources/manufacturers.md) | |
| [notifications](resources/notifications.md) | |
| [price_calculators](resources/price_calculators.md) | rules |
| [price_calculator_rules](resources/price_calculator_rules.md) | modifiers |
| [price_calculator_rule_modifiers](resources/price_calculator_rule_modifiers.md) | |
| [products](resources/products.md) | variants, personalizations, related, categories, pricing, attributes, variant\_inventory, pictures, child\_products, shipping\_rate\_adjustments, reviews, custom\_fields |
| [product_lists](resources/product_lists.md) | |
| [product_pictures](resources/product_pictures.md) | |
| [product_reviews](resources/product_reviews.md) | ratings |
| [product_statuses](resources/product_statuses.md) | |
| [product_variants](resources/product_variants.md) | |
| [shipping_rate_adjustments](resources/shipping_rate_adjustments.md) | |
| [variant_groups](resources/variant_groups.md) | variants |
| [variant_inventory](resources/variant_inventory.md) | pricing, variants |

\* Special endpoint

### Content

| Name | Collections |
| ---- | ----------- |
| [blogs](resources/blogs.md) | categories, posts |
| [blog_categories](resources/blog_categories.md) | posts |
| [blog_posts](resources/blog_posts.md) | categories |
| [links](resources/links.md) | child_links |
| [pages](resources/pages.md) | |

### Marketing

| Name | Collections |
| ---- | ----------- |
| [adcodes](resources/adcodes.md) | |
| [affiliates](resources/affiliates.md) | |
| [coupon_codes](resources/coupon_codes.md) | |
| [discount_methods](resources/discount_methods.md) | rules |
| [discount_rules](resources/discount_rules.md) | |
| [drips](resources/drips.md) | members, events |
| [email_templates](resources/email_templates.md) | |
| [gift_certificates](resources/gift_certificates.md) | transactions |
| [gift_certificate_transactions](resources/gift_certificate_transactions.md) | |
| [mailing_lists](resources/mailing_lists.md) | members |

### Tools

| Name | Collections |
| ---- | ----------- |
| [custom_fields](resources/custom_fields.md) | values, list_items, stores |
| [custom\_field\_values](resources/custom_field_values.md) | |

### Settings

| Name | Collections |
| ---- | ----------- |
| [custom_shipping_methods](resources/custom_shipping_methods.md)	| rules |
| [payment_methods](resources/payment_methods.md)	| fields, stores |
| [regions](resources/regions.md)	| |
| [shipping_providers](resources/shipping_providers.md)	| services |
| [tax_rates](resources/tax_rates.md)	| |
| [url_redirects](resources/url_redirects.md)	| |
| [warehouses](resources/warehouses.md)	| |

### System

| Name | Collections |
| ---- | ----------- |
| [sessions](resources/sessions.md)	| |
| [stores](resources/stores.md)	| |
