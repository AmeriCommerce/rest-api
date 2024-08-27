blog_posts
==========

```shell
GET /api/v1/blog_posts
```

**Required scope**: `read_content`, `content`

Sample Model
------------

```json
{
	"id": 1,
	"blog_id": 1,
	"title": "Lorem ipsum",
	"keywords": "",
	"description": "",
	"content": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>",
	"published_at": "2014-03-05T08:34:00-06:00",
	"updated_at": "2014-03-05T08:46:30.713-06:00",
	"created_at": "2014-03-05T08:36:18.377-06:00",
	"teaser_title": "Lorem ipsum",
	"teaser_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
	"post_image_url": "",
	"teaser_image_url": "",
	"author_profile_id": 1,
	"are_comments_enabled": false,
	"is_featured": false,
	"is_stickied": false,
	"are_comments_locked": false,
	"view_count": 6,
        "store_id": 1,
        "head_tags": "",
        "url_rewrite": "",
        "page_title": "",
        "page_content_type": "BlogPost"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/blogs/{id}/{nested_resource}`.

### categories

```shell
GET /api/v1/blog_posts?expand=categories
```

```shell
GET /api/v1/blog_posts/{id}/categories
```

```json
{
	...
	"categories": [
		{
			"id": 1,
                        "blog_id": 1,
	                "parent_category_id": 0,
	                "type": "Tag",
	                "description": "",
	                "updated_at": "2014-03-05T08:46:30.627-06:00",
	                "created_at": "2014-03-05T08:46:30.627-06:00",
	                "name": "test",
	                "blog_category_path": ""
		},
		...
	],
	...
}
```