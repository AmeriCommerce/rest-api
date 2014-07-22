addresses
=========

```shell
GET /api/v1/addresses
```

**Required scope**: `read_people`, `people`

Sample Model
------------

```json
{
	"id": 1,
	"customer_id": 1,
	"address_line_1": "1234 AmeriCommerce Blvd",
	"address_line_2": "Suite 1",
	"city": "Beaumont",
	"state": "Texas",
	"postal_code": "77702",
	"country": "United States",
	"is_default_shipping_address": false
	"phone": "555-555-5555",
	"company": "AmeriCommerce",
	"alternate_phone": "",
	"fax": "",
	"comments": "",
	"is_default_billing_address": false,
	"updated_at": "2014-04-07T11:55:56.297-05:00",
	"created_at": "2014-04-07T11:55:56.297-05:00",
	"first_name": "Chris",
	"last_name": "Allen"
}
```