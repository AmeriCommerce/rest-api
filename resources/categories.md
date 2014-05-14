categories
==========

```shell
GET /api/v1/categories
```

Sample Model
------------

```json
{
	"id": 1,
	"name": "Shoes",
	"short_description": "",
	"sort_order": 0,
	"is_hidden": false,
	"parent_category_id": 14,
	"max_quantity": 0,
	"category_thumbnail": "",
	"page_title": "",
	"keywords": "",
	"meta_description": "",
	"category_image": "",
	"external_content_url": "",
	"is_category_content_displayed": true,
	"are_subcategory_products_displayed": false,
	"url_rewrite": "",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"default_product_picture": "",
	"alternate_thumbnail": "",
	"head_tags": ""
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/categories/{id}/{nested_resource}`.

### products