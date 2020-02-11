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

* [addresses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/addresses.md)
* [customers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/customers.md)
* [customer_types](https://github.com/AmeriCommerce/rest-api/blob/master/resources/customer_types.md)
* [customer_payment_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/customer_payment_methods.md)
* [profiles](https://github.com/AmeriCommerce/rest-api/blob/master/resources/profiles.md)
* [users](https://github.com/AmeriCommerce/rest-api/blob/master/resources/users.md)

Orders
------

Permissions required: `Orders`, `OrderStatuses`

* `read_orders` - View order data
* `orders` - View and change order data; supercedes `read_order` if specified together

Applies to:

* [carts](https://github.com/AmeriCommerce/rest-api/blob/master/resources/carts.md)
* [cart_items](https://github.com/AmeriCommerce/rest-api/blob/master/resources/cart_items.md)
* [credit_cards](https://github.com/AmeriCommerce/rest-api/blob/master/resources/credit_cards.md)
* [orders](https://github.com/AmeriCommerce/rest-api/blob/master/resources/orders.md)
* [order_addresses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_addresses.md)
* [order_items](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_items.md)
* [order_payments](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_payments.md)
* [order_shipments](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_shipments.md)
* [order_statuses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_statuses.md)
* [quotes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/quotes.md)
* [subscriptions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/subscriptions.md)

Catalog
-------

Permissions required: `Products`, `ProductStatuses`, `VariationGroups`, `ProductAttributes`, `Categories`, `Manufacturers`

* `read_catalog` - View catalog data
* `catalog` - View and change catalog data; supercedes `read_catalog` if specified together

Applies to:

* [attributes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/attributes.md)
* [attribute_groups](https://github.com/AmeriCommerce/rest-api/blob/master/resources/attribute_groups.md)
* [categories](https://github.com/AmeriCommerce/rest-api/blob/master/resources/categories.md)
* [manufacturers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/manufacturers.md)
* [products](https://github.com/AmeriCommerce/rest-api/blob/master/resources/products.md)
* [product_lists](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_lists.md)
* [product_pictures](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_pictures.md)
* [product_statuses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_statuses.md)
* [product_variants](https://github.com/AmeriCommerce/rest-api/blob/master/resources/product_variants.md)
* [shipping_rate_adjustments](https://github.com/AmeriCommerce/rest-api/blob/master/resource/shipping_rate_adjustments.md)
* [variant_groups](https://github.com/AmeriCommerce/rest-api/blob/master/resources/variant_groups.md)
* [variant_inventory](https://github.com/AmeriCommerce/rest-api/blob/master/resources/variant_inventory.md)

Content
-------

Permissions required: `Blogs`, `BlogCategories`, `BlogPosts`, `ContentManagement`, `UrlRedirecting`

* `read_content` - View blog, page, and other content-related data
* `content` - View and change blog, page, and other content-related data; supercedes `read_content` if specified together

Applies to:

* [blogs](https://github.com/AmeriCommerce/rest-api/blob/master/resources/blogs.md)
* [blog_categories](https://github.com/AmeriCommerce/rest-api/blob/master/resources/blog_categories.md)
* [blog_posts](https://github.com/AmeriCommerce/rest-api/blob/master/resources/blog_posts.md)
* [links](https://github.com/AmeriCommerce/rest-api/blob/master/resources/links.md)
* [pages](https://github.com/AmeriCommerce/rest-api/blob/master/resources/pages.md)

Marketing
---------

Permissions required: `AdCodes`, `Affiliates`, `EmailEditor`, `MailingList`, `DiscountMethods`, `GiftCertificates`

* `read_marketing` - View adcode, discount, and other marketing-related data
* `marketing` - View and change adcode, discount, and other marketing-related data; supercedes `read_marketing` if specified together

Applies to:

* [adcodes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/adcodes.md)
* [affiliates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/affiliates.md)
* [coupon_codes](https://github.com/AmeriCommerce/rest-api/blob/master/resources/coupon_codes.md)
* [discount_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/discount_methods.md)
* [discount_rules](https://github.com/AmeriCommerce/rest-api/blob/master/resources/discount_rules.md)
* [drips](https://github.com/AmeriCommerce/rest-api/blob/master/resources/drips.md)
* [email_templates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/email_templates.md)
* [gift_certificates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/gift_certificates.md)
* [gift_certificate_transactions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/gift_certificate_transactions.md)
* [mailing_lists](https://github.com/AmeriCommerce/rest-api/blob/master/resources/mailing_lists.md)

Specialized Scopes
------------------

### email

Permissions required: `EmailEditor`

Applies to:

* `POST /api/v1/email_templates/{id}/send`

### custom_fields

Permissions required: `CustomFields`

Applies to:

* [custom_fields](https://github.com/AmeriCommerce/rest-api/blob/master/resources/custom_fields.md)

### settings

Permissions required: `Shipping`, `Warehouses`, `TaxRates`, `GlobalRegions`, `PaymentGateways`, `UrlRedirecting`

Applies to:

* [custom_shipping_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/custom_shipping_methods.md)
* [payment_methods](https://github.com/AmeriCommerce/rest-api/blob/master/resources/payment_methods.md)
* [regions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/regions.md)
* [shipping_providers](https://github.com/AmeriCommerce/rest-api/blob/master/resources/shipping_providers.md)
* [tax_rates](https://github.com/AmeriCommerce/rest-api/blob/master/resources/tax_rates.md)
* [url_redirects](https://github.com/AmeriCommerce/rest-api/blob/master/resources/url_redirects.md)
* [warehouses](https://github.com/AmeriCommerce/rest-api/blob/master/resources/warehouses.md)

### system

Permissions required: `FileBrowser`, `Sessions`, `StoreSettings`

Applies to:

* [stores](https://github.com/AmeriCommerce/rest-api/blob/master/resources/stores.md)
* [sessions](https://github.com/AmeriCommerce/rest-api/blob/master/resources/sessions.md)
* `POST /api/v1/upload`

### decrypt

Allows sensitive information to be decrypted. The authorizing user must have access to view this information. Tokens with this scope must be regenerated every 90 days if combined with `no_expiry`.

Applies to:

* `GET /api/v1/credit_cards/{id}/decrypted`
* `GET /api/v1/order_payments/{id}/decrypted`

### no_expiry

Token does not expire and does not require a `refresh_token`.
