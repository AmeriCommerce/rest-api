regions
=======

```shell
GET /api/v1/regions
```

**Required scope**: `settings`

Sample Model
------------

```json
{
	"id": 1,
	"postal_codes": [],
	"name": "North America",
	"states": [],
	"countries": [
		"United States",
		"Canada"
	],
	"markup_type": "Percent",
	"markup_amount": 0,
	"sort_order": 0,
	"updated_at": "2014-05-06T12:24:32.753-05:00",
	"created_at": "2014-05-06T12:24:32.753-05:00",
	"region_type": "Country",
	"postal_code_country": null,
	"is_shipping_region": true,
	"is_tax_region": true
}
```