links
=====

```shell
GET /api/v1/links
```

Sample Model
------------

```json
{
	"id": 32,
	"url": "http://www.google.com",
	"text": "google",
	"sort_order": null,
	"store_id": 3,
	"is_hidden": false,
	"named_link": null,
	"page_id": 0,
	"updated_at": "2014-07-21T14:44:40.68-05:00",
	"created_at": "2014-07-21T14:44:40.68-05:00",
	"category_id": 0,
	"is_dynamic_menu_root": false,
	"dynamic_menu_levels": 0,
	"link_type": "ExternalUrl",
	"parent_link_id": 28,
	"is_hidden_in_navigation_only": false,
	"opens_in_new_window": false,
	"is_home_page": false,
	"product_id": 0,
	"blog_id": 0,
	"blog_category_id": 0
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/links/{id}/{nested_resource}`.

### child_links

```shell
GET /api/v1/links?expand=child_links
```

```shell
GET /api/v1/links/{id}/child_links
```

```json
{
	...
	"child_links": [
		{
			"id": 30,
			"url": "",
			"text": "cool stuff",
			"sort_order": null,
			"store_id": 3,
			"is_hidden": false,
			"named_link": null,
			"page_id": 0,
			"updated_at": "2014-07-21T14:43:07.553-05:00",
			"created_at": "2014-07-21T14:43:07.553-05:00",
			"category_id": 2,
			"is_dynamic_menu_root": false,
			"dynamic_menu_levels": 0,
			"link_type": "Category",
			"parent_link_id": 28,
			"is_hidden_in_navigation_only": false,
			"opens_in_new_window": false,
			"is_home_page": false,
			"product_id": 0,
			"blog_id": 0,
			"blog_category_id": 0
		},
		{
			"id": 31,
			"url": "",
			"text": "all the cats",
			"sort_order": null,
			"store_id": 3,
			"is_hidden": false,
			"named_link": "Category Listing",
			"page_id": 0,
			"updated_at": "2014-07-21T14:44:10.173-05:00",
			"created_at": "2014-07-21T14:44:10.173-05:00",
			"category_id": 0,
			"is_dynamic_menu_root": false,
			"dynamic_menu_levels": 0,
			"link_type": "StorefrontPage",
			"parent_link_id": 28,
			"is_hidden_in_navigation_only": false,
			"opens_in_new_window": false,
			"is_home_page": false,
			"product_id": 0,
			"blog_id": 0,
			"blog_category_id": 0
		},
		...
	],
	...
}
```