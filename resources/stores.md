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
	"is_micro_store": false,
	"parent_store_id": 0,
	"profile_id": 9
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

