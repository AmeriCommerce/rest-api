Resource List
=============

All API URLs start with `https://[mystorename.com]/api/v1/`, where `[mystorename.com]` is the SSL domain name of your Cart.com Online Store. See [Common Usage](common_usage.md) for a more detailed explanation of most of the operations these provide.

### People

| Name | Collections |
| ---- | ----------- |
| [addresses](docs/resources/addresses.md) |
| [customers](docs/resources/customers.md) | addresses, reward\_points, custom\_fields |
| [customer_association](docs/resources/customer_association.md) | |
| [customer_types](docs/resources/customer_types.md) | |
| [customer_payment_methods](docs/resources/customer_payment_methods.md) | fields |
| [profiles](docs/resources/profiles.md) | contacts |
| [users](docs/resources/users.md) | |

### Orders

| Name | Collections |
| ---- | ----------- |
| [carts](docs/resources/carts.md) | items |
| [cart_items](docs/resources/cart_items.md) | child_items |
| [credit_cards](docs/resources/credit_cards.md) | |
| [orders](docs/resources/orders.md) | items, payments, shipments, custom_fields |
| [order_addresses](docs/resources/order_addresses.md) | |
| [order_items](docs/resources/order_items.md) | |
| [order_payments](docs/resources/order_payments.md) | fields |
| [order_shipments](docs/resources/order_shipments.md) | items |
| [order_statuses](docs/resources/order_statuses.md) | |
| [quotes](docs/resources/quotes.md) | items, payments, shipments, custom_fields |
| [subscriptions](docs/resources/subscriptions.md) | |
| [wishlists](docs/resources/wishlists.md) | items |

### Catalog

| Name | Collections |
| ---- | ----------- |
| [attributes](docs/resources/attributes.md) | |
| [attribute_groups](docs/resources/attribute_groups.md) | |
| [categories](docs/resources/categories.md) | products, custom_fields |
| [inventory](docs/resources/inventory.md)* | |
| [manufacturers](docs/resources/manufacturers.md) | |
| [notifications](docs/resources/notifications.md) | |
| [price_calculators](docs/resources/price_calculators.md) | rules |
| [price_calculator_rules](docs/resources/price_calculator_rules.md) | modifiers |
| [price_calculator_rule_modifiers](docs/resources/price_calculator_rule_modifiers.md) | |
| [products](docs/resources/products.md) | variants, personalizations, related, categories, pricing, attributes, variant\_inventory, pictures, child\_products, shipping\_rate\_adjustments, reviews, custom\_fields |
| [product_lists](docs/resources/product_lists.md) | |
| [product_pictures](docs/resources/product_pictures.md) | |
| [product_reviews](docs/resources/product_reviews.md) | ratings |
| [product_statuses](docs/resources/product_statuses.md) | |
| [product_variants](docs/resources/product_variants.md) | |
| [shipping_rate_adjustments](docs/resources/shipping_rate_adjustments.md) | |
| [variant_groups](docs/resources/variant_groups.md) | variants |
| [variant_inventory](docs/resources/variant_inventory.md) | pricing, variants |

\* Special endpoint

### Content

| Name | Collections |
| ---- | ----------- |
| [blogs](docs/resources/blogs.md) | categories, posts |
| [blog_categories](docs/resources/blog_categories.md) | posts |
| [blog_posts](docs/resources/blog_posts.md) | categories |
| [links](docs/resources/links.md) | child_links |
| [pages](docs/resources/pages.md) | |

### Marketing

| Name | Collections |
| ---- | ----------- |
| [adcodes](docs/resources/adcodes.md) | |
| [affiliates](docs/resources/affiliates.md) | |
| [coupon_codes](docs/resources/coupon_codes.md) | |
| [discount_methods](docs/resources/discount_methods.md) | rules |
| [discount_rules](docs/resources/discount_rules.md) | |
| [drips](docs/resources/drips.md) | members, events |
| [email_templates](docs/resources/email_templates.md) | |
| [gift_certificates](docs/resources/gift_certificates.md) | transactions |
| [gift_certificate_transactions](docs/resources/gift_certificate_transactions.md) | |
| [mailing_lists](docs/resources/mailing_lists.md) | members |

### Tools

| Name | Collections |
| ---- | ----------- |
| [custom_fields](docs/resources/custom_fields.md) | values, list_items, stores |
| [custom\_field\_values](docs/resources/custom_field_values.md) | |

### Settings

| Name | Collections |
| ---- | ----------- |
| [custom_shipping_methods](docs/resources/custom_shipping_methods.md)	| rules |
| [payment_methods](docs/resources/payment_methods.md)	| fields, stores |
| [regions](docs/resources/regions.md)	| |
| [shipping_providers](docs/resources/shipping_providers.md)	| services |
| [tax_rates](docs/resources/tax_rates.md)	| |
| [url_redirects](docs/resources/url_redirects.md)	| |
| [warehouses](docs/resources/warehouses.md)	| |

### System

| Name | Collections |
| ---- | ----------- |
| [sessions](docs/resources/sessions.md)	| |
| [stores](docs/resources/stores.md)	| |
| [microstores](docs/resources/microstores.md)	| |
