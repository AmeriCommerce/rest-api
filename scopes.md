Scopes
======

Many of the API scopes are segmented similarly to the admin console. There are some special ones that cover more specific functionality. An access token can only use the scopes that are requested by the application when the token is being created. To change the scope, a new token must be obtained.

People
------

* `read_people` - View customer, user, or profile data
* `people` - View and change customer, user, or profile data; supercedes `read_customer` if specified together

Orders
------

* `read_order` - View order data
* `order` - View and change order data; supercedes `read_order` if specified together

Catalog
-------

* `read_catalog` - View catalog data
* `catalog` - View and change catalog data; supercedes `read_catalog` if specified together

Content
-------

* `read_content` - View blog, page, and other content-related data
* `content` - View and change blog, page, and other content-related data; supercedes `read_content` if specified together

Marketing
---------

* `read_marketing` - View adcode, discount, and other marketing-related data
* `marketing` - View and change adcode, discount, and other marketing-related data; supercedes `read_marketing` if specified together

Tools
-----

* `email` - Send email on behalf of the store
* `custom_fields` - Manage custom fields

Other
-----

* `system` - Perform system tasks such as uploading files to the site
* `decrypt` - Access to decrypt certain sensitive information, cannot be combined with `no_expiry`
* `no_expiry` - Token does not expire and does not require a refresh token, cannot be combined with `decrypt`