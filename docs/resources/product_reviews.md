product\_reviews
================

```shell
GET /api/v1/product_reviews
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 1,
	"product_id": 55,
	"title": "This product is awesome",
	"body": "I have no bad things to say about it",
	"review_pros": "",
	"review_cons": "",
	"overall_rating": 5,
	"customer_id": null,
	"approved_by_user_id": null,
	"approved_at": null,
	"created_at": "2014-04-16T13:35:20.6-05:00",
	"updated_at": "2014-04-16T13:35:20.6-05:00",
	"author_display_name": "sfsdfsdfsd",
	"author_email": "test@blah.com",
	"author_website": "",
	"author_location": "",
	"approval_status": "Approved",
	"origin_store_id": 3,
	"profile_id": 12
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/product_reviews/{id}/{nested_resource}`.

### ratings

```shell
GET /api/v1/product_reviews?expand=ratings
```

```shell
GET /api/v1product_reviews/{id}/ratings
```

```json
{
	...
	"ratings": [
		{
			"name": "quality",
			"description": "Build Quality",
			"rating": 5
		},
		{
			"name": "overall",
			"description": "Overall Satisfaction",
			"rating": 3
		},
		...
	],
	...
}
```