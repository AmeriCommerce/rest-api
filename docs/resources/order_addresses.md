order_addresses
===============

```shell
GET /api/v1/order_addresses
```

**Required scope**: `read_orders`, `orders`

Sample Model
------------

```json
{
	"id": 1,
	"customer_id": 1,
	"company": "AmeriCommerce",
	"address_line_1": "1234 AmeriCommerce Blvd",
	"address_line_2": "Suite 1",
	"city": "Beaumont",
	"state": "Texas",
	"postal_code": 77702,
	"country": "United States",
	"phone": "555-555-5555",
	"alternate_phone": "",
	"fax": "",
	"comments": "",
	"updated_at": "2014-02-18T13:36:58.357-06:00",
	"created_at": "2014-02-18T13:36:58.357-06:00",
	"first_name": "Chris",
	"last_name": "Allen"
}
```