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
        "address_type": "Default",
        "state_code": "TX",
        "country_code": "US"
}
```

Store Location Order Address
--------------------

This is used to create an order address from a store location address. If used, the first_name, last_name, and phone fields will override the values returned from the existing customer record when creating the order address.

###### Example Request

```Shell
POST /api/v1/order_addresses/store_location_address
```

```json
{
        "location_id": 1,
        "customer_id": 6,
        "first_name": "",
        "last_name": "",
        "phone": ""
}
```

###### Example Response

```json
{
        "id": 234,
	"customer_id": 6,
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
        "address_type": "Default",
        "state_code": "TX",
        "country_code": "US" 
}
```