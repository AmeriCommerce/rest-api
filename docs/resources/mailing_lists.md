mailing_lists
=============

```shell
GET /api/v1/mailing_lists
```

**Required scope**: `read_marketing`, `marketing`

Sample Model
------------

```json
{
	"id": 1,
	"type": "Internal",
	"admin_list_name": "InternalList",
	"public_list_name": "",
	"store_id": 1,
	"is_store_default": true,
	"auto_opt_in": false,
	"is_hidden": false,
	"url_based_subscribe_url": "",
	"updated_at": null,
	"created_at": null,
	"welcome_email_template_id": null
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/mailing_lists/{id}/{nested_resource}`.

### members

```shell
GET /api/v1/mailing_lists?expand=members
```

```shell
GET /api/v1/mailing_lists/{id}/members
```

```json
{
	...
	"members": [
		{
		        "id": 8,
                        "mailing_list_id": 1,
                        "customer_id": 14,
                        "is_subscribed": true,
                        "updated_at": "2024-08-15T11:27:27.043-05:00",
                        "created_at": "2024-08-15T11:27:27.043-05:00"
		},
		...
	],
	...
}
```