customers
=========

```shell
GET /api/v1/customers
```

**Required scope**: `read_people`, `people`

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
	"customer_type_id": 1,
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
	"source_group": "",
	"sales_person_user_id": 2,
	"store_payment_methods_enabled": ["Purchase Orders","Checks"],
	"tax_rate": 2,
	"lock_default_address": false,
	"reward_tier_id": 1,
	"payment_net_term": 0,
	"credit_limit": 10.00,
	"is_inactive": false,
	"use_shared_credit_limit": false,
	"override_shared_credit_limit": false,
	"customer_payment_methods_availability": [
		{
			"id": 5,
			"payment_method_id": 6,
			"store_payment_method_id": 12,
			"status": "Active",
			"customer_id": 1
		}
	],
	"default_payment_type_name": "Credit Card"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/customers/{id}/{nested_resource}`.

### additional_emails

```shell
GET /api/v1/customers?expand=additional_emails
```

```shell
GET /api/v1/customers/{id}/additional_emails
```

```json
{
	...
	"customer_additional_emails": [
		{
			"customer_additional_email_id": 1,
			"customer_id": 13,
			"email": "test@not-real-address.zzz"
		},
		...
	],
	...
}
```

### addresses

```shell
GET /api/v1/customers?expand=addresses
```

```shell
GET /api/v1/customers/{id}/addresses
```

```json
{
	...
	"addresses": [
		{
			"id": 42,
                        "customer_id": 13,
                        "address_line_1": "251 N Bristol Ave",
                        "address_line_2": "",
                        "city": "Los Angeles",
                        "state": "California",
                        "postal_code": "90049",
                        "country": "United States",
                        "is_default_shipping_address": false,
                        "phone": "1234567897",
                        "company": "",
                        "alternate_phone": "",
                        "fax": "",
                        "comments": "",
                        "is_default_billing_address": false,
                        "updated_at": "2019-04-01T17:12:37.187-05:00",
                        "created_at": "2019-04-01T17:12:37.107-05:00",
                        "first_name": "Will",
                        "last_name": "Smith",
                        "address_type": "Default"
		},
		...
	],
	...
}
```

### custom_fields

```shell
GET /api/v1/customers?expand=custom_fields
```

```shell
GET /api/v1/customers/{id}/custom_fields
```

```json
{
	...
	"custom_fields": [
		{
		    "name": "CustomerCustomField",
                    "value": ""
		},
		...
	],
	...
}
```


### customer_store_locations

```shell
GET /api/v1/customers?expand=customer_store_locations
```

```shell
GET /api/v1/customers/{id}/customer_store_locations
```

```json
{
	...
	"customer_store_locations": [
		{
		    "id": 7,
                    "store_location_id": 3,
                    "customer_id": 13
		},
		...
	],
	...
}
```

### reward_points

```shell
GET /api/v1/customers?expand=reward_points
```

```shell
GET /api/v1/customers/{id}/reward_points
```

```json
{
	...
	"reward_points": [
		{
			"id": 11,
			"customer_id": 13,
			"transaction_type": "AssignedBySiteOwner",
			"earned_at": "2023-06-30T14:22:44.87-05:00",
			"points_earned": 1000,
			"points_remaining": 1000,
			"note": "",
			"order_id": 100013,
			"created_at": "2023-06-30T14:22:44.883-05:00",
			"updated_at": "2023-06-30T14:22:44.883-05:00",
			"status": "Active",
			"expires_at": "2023-07-31T15:00:21.4-05:00"
		},
		...
	],
	...
}
```