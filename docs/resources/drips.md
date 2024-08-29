drips
=====

```shell
GET /api/v1/drips
```

**Required scope**: `read_marketing`, `marketing`

Sample Model
------------

```json
{
	"id": 1,
	"name": "test",
	"is_enabled": false
}
```

## Add Customer To Drip Series

###### Example Request
```shell
POST /api/v1/drips/{id}/members
```

```json
{
    "customer_ids": [6,8]
}
```

###### Example Response
```json
{
        "id": 1,
        "name": "test",
        "is_enabled": true,
	"members": [
		{
		        "id": 1,
                        "drip_id": 1,
                        "customer_id": 6,
                        "started_at": "2022-04-30T00:00:00-05:00",
                        "completed_at": null,
                        "last_email_at": null,
                        "email_count": 0,
                        "subscription_id": null,
                        "order_id": null,
                        "custom_merge_keys": "",
                        "custom_merge_values": ""
		},
                {
		        "id": 1,
                        "drip_id": 1,
                        "customer_id": 8,
                        "started_at": "2022-04-30T00:00:00-05:00",
                        "completed_at": null,
                        "last_email_at": null,
                        "email_count": 0,
                        "subscription_id": null,
                        "order_id": null,
                        "custom_merge_keys": "",
                        "custom_merge_values": ""
		},
		...
	],
	...
}
```

## Remove Customer From Drip Series

Removing a customer from a drip series will not remove them from the member's list, instead it will mark the drip series as complete for that customer.

###### Example Request
```shell
DELETE /api/v1/drips/{id}/members
```

```json
{
    "customer_ids": [6,8]
}
```

###### Example Response
```json
{
        "id": 1,
        "name": "test",
        "is_enabled": true,
	"members": [
		{
		        "id": 1,
                        "drip_id": 1,
                        "customer_id": 6,
                        "started_at": "2022-04-30T00:00:00-05:00",
                        "completed_at": "2022-05-30T00:00:00-05:00",
                        "last_email_at": "2022-05-10T00:00:00-05:00",
                        "email_count": 3,
                        "subscription_id": null,
                        "order_id": null,
                        "custom_merge_keys": "",
                        "custom_merge_values": ""
		},
                {
		        "id": 1,
                        "drip_id": 1,
                        "customer_id": 8,
                        "started_at": "2022-04-30T00:00:00-05:00",
                        "completed_at": "2022-05-30T00:00:00-05:00",
                        "last_email_at": "2022-05-15T00:00:00-05:00",
                        "email_count": 5,
                        "subscription_id": null,
                        "order_id": null,
                        "custom_merge_keys": "",
                        "custom_merge_values": ""
		},
		...
	],
	...
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/drips/{id}/{nested_resource}`.

### members

```shell
GET /api/v1/drips?expand=members
```

```shell
GET /api/v1/drips/{id}/members
```

```json
{
	...
	"members": [
		{
		        "id": 1,
                        "drip_id": 1,
                        "customer_id": 6,
                        "started_at": "2022-04-30T00:00:00-05:00",
                        "completed_at": "2023-06-23T13:50:17.673-05:00",
                        "last_email_at": "2023-05-26T12:50:09.02-05:00",
                        "email_count": 7,
                        "subscription_id": 1,
                        "order_id": 100013,
                        "custom_merge_keys": "",
                        "custom_merge_values": ""
		},
		...
	],
	...
}
```

### events

```shell
GET /api/v1/drips?expand=events
```

```shell
GET /api/v1/drips/{id}/events
```

```json
{
	...
	"events": [
		{
		        "id": 2,
                        "drip_id": 1,
                        "step_name": "Renewal",
                        "action": "AutoSentEmail",
                        "when_value": 1,
                        "when_interval": "Minutes",
                        "when_event": "BeforeNextSubscriptionRecurs",
                        "sort_order": 2
		},
		...
	],
	...
}
```