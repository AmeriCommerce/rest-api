mailing_lists
=============

```shell
GET /api/v1/mailing_lists
```

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