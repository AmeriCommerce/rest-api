custom_fields
=============

```shell
GET /api/v1/custom_fields
```

**Required scope**: `custom_fields`

Sample Model
------------

```json
{
	"id": 1,
	"updated_at": "2013-12-02T11:09:18.803-06:00",
	"created_at": "2013-12-02T10:58:33-06:00",
	"name": "testdate",
	"resource_type": "Orders",
	"input_type": "DatePicker",
	"value_type": "Date",
	"field_width": 0,
	"sort_order": 0,
	"format_string": "",
	"is_searchable": false,
	"is_editable": false,
	"is_multi_select": false,
	"label": "Test",
	"is_private": false,
	"is_required": true,
	"show_on_order_page": false,
	"display_location": "DefaultLocation",
	"default_value": "",
	"read_only": "Off",
	"show_on_one_page_checkout": false,
        "is_visible_all_stores": true
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/custom_fields/{id}/{nested_resource}`.

### list_items

###### Example Request
```shell
GET /api/v1/custom_fields?expand=list_items
```

```shell
GET /api/v1/custom_fields/{id}/list_items
```

```json
{
	...
	"list_items": [
		{
			"id": 10,
                        "custom_field_id": 1,
                        "text": "test",
                        "value": "test",
                        "sort_order": 0
		},
		...
	],
	...
}
```

### stores

###### Example Request
```shell
GET /api/v1/custom_fields?expand=stores
```

```shell
GET /api/v1/custom_fields/{id}/stores
```

```json
{
	...
	"stores": [
		{
			"id": 1,
                        "name": "Your Site"
		},
		...
	],
	...
}
```

### values

###### Example Request
```shell
GET /api/v1/custom_fields?expand=values
```

```shell
GET /api/v1/custom_fields/{id}/values
```

```json
{
	...
	"values": [
		{
			"id": 2,
	                "custom_field_id": 1,
	                "resource_id": 100013,
	                "value": "2/5/2014",
	                "updated_at": "2014-02-18T13:37:19.25-06:00",
	                "created_at": "2014-02-18T13:37:19.25-06:00"
		},
		...
	],
	...
}
```