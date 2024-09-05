stores
======

## Get Stores

This resource is read only (only `GET` actions are available).

###### Example Request
```shell
GET /api/v1/stores
```

**Required scope**: `system`

###### Example Response

```json
{
	"id": 1,
	"name": "localhost",
	"domain_name": "localhost",
	"email": "test@not-my-real-address.zzz",
	"keywords": "",
	"description": "",
        "address_line_1": "123 Main",
        "address_line_2": "",
        "city": "Beaumont",
        "state": "Texas",
        "country": "United States",
        "postal_code": "77702",
        "phone": "1234567890",
        "fax": "",
        "all_catalog": true,
	"is_micro_store": false,
	"parent_store_id": 0,
        "company_name": "",
        "billing_first_name": "",
        "billing_last_name": "",
        "tech_first_name": "",
        "tech_last_name": "",
        "tech_email": "",
        "tech_same_as_billing": false,
	"profile_id": 9,
        "store_logo": "",
        "store_image": "",
        "average_testimonial_rating": 4.00,
        "testimonial_count": 6
}
```

## Get Store Alert Emails

###### Example Request
```shell
GET /api/v1/stores/{store_id}/store_alert_email
```
###### Example Response

```json
{
    "total_count": 3,
    "store_alert_email": [
        {
            "id": 2,
            "store_id": 3,
            "email": "test@not-real-address.com"
        },
        {
            "id": 3,
            "store_id": 3,
            "email": "test2@not-real-address.com"
        }
    ]
}
```

## Add Store Alert Emails

###### Example Request
```shell
PUT /api/v1/stores/{store_id}/store_alert_email
```

```json
{
    "email": "test@not-real-address.com"
}
```
###### Example Response
```json
{
    "id": 5,
    "store_id": 3,
    "email": "test@not-real-address.com"
}
```

## Get Store Active Catalog

###### Example Request

```shell
GET /api/v1/stores/{id}/active_catalog
```

###### Example Response

```json
{
    "store_id": 1,
    "is_micro_store": false,
    "microstore_catalog_override": false,
    "root_category_id": 0,
    "category_ids": [
        1,
        3
    ],
    "product_ids": []
}
```

## Update Store Active Catalog

###### Example Request
```shell
PUT /api/v1/stores/{id}/active_catalog
```

```json
{
    "root_category_id": 3,
    "category_ids": [
        3,
        1,
        9,
        8
    ],
    "product_ids": []
}
```

###### Example Response

```json
{
    "store_id": 1,
    "is_micro_store": false,
    "microstore_catalog_override": false,
    "root_category_id": 3,
    "category_ids": [
        3,
        1,
        9,
        8
    ],
    "product_ids": []
}
```
