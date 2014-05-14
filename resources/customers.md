customers
=========

```shell
GET /api/v1/customers
```

Sample Model
------------

```json
{
	"id": 1,
	"customer_number": "",
	"last_name": "Allen",
	"first_name": "Chris",
	"email": "test@not-my-real-address.zzz",
	"phone_number": "555-555-5555",
	"registered_at": "2004-10-08T00:00:00-05:00",
	"last_visit_at": "2005-09-08T13:48:55-05:00",
	"adcode": "",
	"adcode_id": 0,
	"affiliate_id": 0,
	"is_no_tax_customer": false,
	"comments": "",
	"store_id": 1,
	"source": "",
	"search_string": "",
	"no_account": false,
	"sales_person": "",
	"alternate_phone_number": "",
	"is_affiliate_customer": false,
	"updated_at": "2005-09-08T13:48:55-05:00",
	"created_at": "2004-10-08T00:00:00-05:00",
	"username": "chris",
	"is_contact_information_only": false,
	"tax_exemption_number": "",
	"company": "AmeriCommerce",
	"source_group": ""
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/customers/{id}/{nested_resource}`.

### addresses

### custom_fields