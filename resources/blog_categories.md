blog_categories
===============

```shell
GET /api/v1/blog_categories
```

Sample Model
------------

```json
{
	"id": 1,
	"blog_id": 1,
	"parent_category_id": 0,
	"type": "Tag",
	"description": "",
	"updated_at": "2014-03-05T08:46:30.627-06:00",
	"created_at": "2014-03-05T08:46:30.627-06:00",
	"name" "test",
	"blog_category_path": ""
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/blog_categories/{id}/{nested_resource}`.

### posts