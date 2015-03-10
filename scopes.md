[//]: # (Zendesk: 202836810)
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

* [addresses](resources/addresses.md)
* [customers](resources/customers.md)
* [customer_types](resources/customer_types.md)
* [customer_payment_methods](resources/customer_payment_methods.md)
* [profiles](resources/profiles.md)
* [users](resources/users.md)

Orders
------

Permissions required: `Orders`, `OrderStatuses`

* `read_orders` - View order data
* `orders` - View and change order data; supercedes `read_order` if specified together

Applies to:

* [carts](resources/carts.md)
* [cart_items](resources/cart_items.md)
* [credit_cards](resources/credit_cards.md)
* [orders](resources/orders.md)
* [order_addresses](resources/order_addresses.md)
* [order_items](resources/order_items.md)
* [order_payments](resources/order_payments.md)
* [order_shipments](resources/order_shipments.md)
* [order_statuses](resources/order_statuses.md)
* [quotes](resources/quotes.md)
* [subscriptions](resources/subscriptions.md)

Catalog
-------

Permissions required: `Products`, `ProductStatuses`, `VariationGroups`, `ProductAttributes`, `Categories`, `Manufacturers`

* `read_catalog` - View catalog data
* `catalog` - View and change catalog data; supercedes `read_catalog` if specified together

Applies to:

* [attributes](resources/attributes.md)
* [attribute_groups](resources/attribute_groups.md)
* [categories](resources/categories.md)
* [manufacturers](resources/manufacturers.md)
* [products](resources/products.md)
* [product_lists](resources/product_lists.md)
* [product_pictures](resources/product_pictures.md)
* [product_statuses](resources/product_statuses.md)
* [product_variants](resources/product_variants.md)
* [shipping_rate_adjustments](resource/shipping_rate_adjustments.md)
* [variant_groups](resources/variant_groups.md)
* [variant_inventory](resources/variant_inventory.md)

Content
-------

Permissions required: `Blogs`, `BlogCategories`, `BlogPosts`, `ContentManagement`, `UrlRedirecting`

* `read_content` - View blog, page, and other content-related data
* `content` - View and change blog, page, and other content-related data; supercedes `read_content` if specified together

Applies to:

* [blogs](resources/blogs.md)
* [blog_categories](resources/blog_categories.md)
* [blog_posts](resources/blog_posts.md)
* [links](resources/links.md)
* [pages](resources/pages.md)

Marketing
---------

Permissions required: `AdCodes`, `Affiliates`, `EmailEditor`, `MailingList`, `DiscountMethods`, `GiftCertificates`

* `read_marketing` - View adcode, discount, and other marketing-related data
* `marketing` - View and change adcode, discount, and other marketing-related data; supercedes `read_marketing` if specified together

Applies to:

* [adcodes](resources/adcodes.md)
* [affiliates](resources/affiliates.md)
* [coupon_codes](resources/coupon_codes.md)
* [discount_methods](resources/discount_methods.md)
* [discount_rules](resources/discount_rules.md)
* [drips](resources/drips.md)
* [email_templates](resources/email_templates.md)
* [gift_certificates](resources/gift_certificates.md)
* [gift_certificate_transactions](resources/gift_certificate_transactions.md)
* [mailing_lists](resources/mailing_lists.md)

Specialized Scopes
------------------

### email

Permissions required: `EmailEditor`

Applies to:

* `POST /api/v1/email_templates/{id}/send`

### custom_fields

Permissions required: `CustomFields`

Applies to:

* [custom_fields](resources/custom_fields.md)

### settings

Permissions required: `Shipping`, `Warehouses`, `TaxRates`, `GlobalRegions`, `PaymentGateways`, `UrlRedirecting`

Applies to:

* [custom_shipping_methods](resources/custom_shipping_methods.md)
* [payment_methods](resources/payment_methods.md)
* [regions](resources/regions.md)
* [shipping_providers](resources/shipping_providers.md)
* [tax_rates](resources/tax_rates.md)
* [url_redirects](resources/url_redirects.md)
* [warehouses](resources/warehouses.md)

### system

Permissions required: `FileBrowser`, `Sessions`, `StoreSettings`

Applies to:

* [stores](resources/stores.md)
* [sessions](resources/sessions.md)
* `POST /api/v1/upload`

### decrypt

Allows sensitive information to be decrypted. The authorizing user must have access to view this information. Tokens with this scope must be regenerated every 90 days if combined with `no_expiry`.

Applies to:

* `GET /api/v1/credit_cards/{id}/decrypted`
* `GET /api/v1/order_payments/{id}/decrypted`

### no_expiry

Token does not expire and does not require a `refresh_token`.
