Scopes
======

Many of the API scopes are segmented similarly to the admin console. There are some special ones that cover more specific functionality. An access token can only use the scopes that are requested by the application when the token is being created. To change the scope, a new token must be obtained.

The user account requesting the access token must have the appropriate role-based privledges in the admin console before they can obtain a token.

People
------

Permissions required: `Customers`, `CustomerTypes`, `UserAccounts`, `StoreSettings`

* `read_people` - View customer, user, or profile data
* `people` - View and change customer, user, or profile data; supercedes `read_customer` if specified together

Applies to:

* [addresses](/acapi.yaml/paths/~1attributes/get)
* [customers](/acapi.yaml/paths/~1customers/get)
* [customer_types](/acapi.yaml/paths/~1customer_types/get)
* [customer_payment_methods](/acapi.yaml/paths/~1customer_payment_methods/get)
* [profiles](/acapi.yaml/paths/~1profiles/get)
* [users](/acapi.yaml/paths/~1users/get)

Orders
------

Permissions required: `Orders`, `OrderStatuses`

* `read_orders` - View order data
* `orders` - View and change order data; supercedes `read_order` if specified together

Applies to:

* [carts](/acapi.yaml/paths/~1carts/get)
* [cart_items](/acapi.yaml/paths/~1cart_items/get)
* [credit_cards](/acapi.yaml/paths/~1credit_cards/get)
* [orders](/acapi.yaml/paths/~1orders/get)
* [order_addresses](/acapi.yaml/paths/~1order_addresses/get)
* [order_items](/acapi.yaml/paths/~1order_items/get)
* [order_payments](/acapi.yaml/paths/~1order_payments/get)
* [order_shipments](/acapi.yaml/paths/~1order_shipments/get)
* [order_statuses](/acapi.yaml/paths/~1order_statuses/get)
* [quotes](/acapi.yaml/paths/~1quotes/get)
* [subscriptions](/acapi.yaml/paths/~1subscriptions/get)

Catalog
-------

Permissions required: `Products`, `ProductStatuses`, `VariationGroups`, `ProductAttributes`, `Categories`, `Manufacturers`

* `read_catalog` - View catalog data
* `catalog` - View and change catalog data; supercedes `read_catalog` if specified together

Applies to:

* [attributes](docs/resources/attributes.md)
* [attribute_groups](docs/resources/attribute_groups.md)
* [categories](docs/resources/categories.md)
* [manufacturers](docs/resources/manufacturers.md)
* [products](docs/resources/products.md)
* [product_lists](docs/resources/product_lists.md)
* [product_pictures](docs/resources/product_pictures.md)
* [product_statuses](docs/resources/product_statuses.md)
* [product_variants](docs/resources/product_variants.md)
* [shipping_rate_adjustments](resource/shipping_rate_adjustments.md)
* [variant_groups](docs/resources/variant_groups.md)
* [variant_inventory](docs/resources/variant_inventory.md)

Content
-------

Permissions required: `Blogs`, `BlogCategories`, `BlogPosts`, `ContentManagement`, `UrlRedirecting`

* `read_content` - View blog, page, and other content-related data
* `content` - View and change blog, page, and other content-related data; supercedes `read_content` if specified together

Applies to:

* [blogs](docs/resources/blogs.md)
* [blog_categories](docs/resources/blog_categories.md)
* [blog_posts](docs/resources/blog_posts.md)
* [links](docs/resources/links.md)
* [pages](docs/resources/pages.md)

Marketing
---------

Permissions required: `AdCodes`, `Affiliates`, `EmailEditor`, `MailingList`, `DiscountMethods`, `GiftCertificates`

* `read_marketing` - View adcode, discount, and other marketing-related data
* `marketing` - View and change adcode, discount, and other marketing-related data; supercedes `read_marketing` if specified together

Applies to:

* [adcodes](docs/resources/adcodes.md)
* [affiliates](docs/resources/affiliates.md)
* [coupon_codes](docs/resources/coupon_codes.md)
* [discount_methods](docs/resources/discount_methods.md)
* [discount_rules](docs/resources/discount_rules.md)
* [drips](docs/resources/drips.md)
* [email_templates](docs/resources/email_templates.md)
* [gift_certificates](docs/resources/gift_certificates.md)
* [gift_certificate_transactions](docs/resources/gift_certificate_transactions.md)
* [mailing_lists](docs/resources/mailing_lists.md)

Specialized Scopes
------------------

### email

Permissions required: `EmailEditor`

Applies to:

* `POST /api/v1/email_templates/{id}/send`

### custom_fields

Permissions required: `CustomFields`

Applies to:

* [custom_fields](docs/resources/custom_fields.md)

### settings

Permissions required: `Shipping`, `Warehouses`, `TaxRates`, `GlobalRegions`, `PaymentGateways`, `UrlRedirecting`

Applies to:

* [custom_shipping_methods](docs/resources/custom_shipping_methods.md)
* [payment_methods](docs/resources/payment_methods.md)
* [regions](docs/resources/regions.md)
* [shipping_providers](docs/resources/shipping_providers.md)
* [tax_rates](docs/resources/tax_rates.md)
* [url_redirects](docs/resources/url_redirects.md)
* [warehouses](docs/resources/warehouses.md)

### system

Permissions required: `FileBrowser`, `Sessions`, `StoreSettings`

Applies to:

* [stores](docs/resources/stores.md)
* [sessions](docs/resources/sessions.md)
* `POST /api/v1/upload`

### decrypt

Allows sensitive information to be decrypted. The authorizing user must have access to view this information. Tokens with this scope must be regenerated every 90 days if combined with `no_expiry`.

Applies to:

* `GET /api/v1/credit_cards/{id}/decrypted`
* `GET /api/v1/order_payments/{id}/decrypted`

### no_expiry

Token does not expire and does not require a `refresh_token`.
