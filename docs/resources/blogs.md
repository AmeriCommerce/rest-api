blogs
=====

```shell
GET /api/v1/blogs
```

**Required scope**: `read_content`, `content`

Sample Model
------------

```json
{
	"id": 1,
	"store_id": 1,
	"name": "My BLarg",
	"description": "",
	"tag_line": "",
	"url_slug": "",
	"meta_description": "",
	"meta_keywords": "",
	"updated_at": "2014-03-05T08:35:35.083-06:00",
	"created_at": "2014-03-05T08:35:35.083-06:00",
	"copyright": "",
	"image_url": "",
	"language": "",
	"max_feed_elements": 25,
	"syndication_type": "Full",
	"is_rss_feed_enabled": true,
	"is_atom_feed_enabled": true,
	"max_chars_short_feed": 250,
	"max_chars_summary": 100,
	"is_commenting_enabled": true,
	"is_comment_moderation_enabled": true,
	"default_post_image": "",
	"default_teaser_image": "",
	"new_post_notification_email_template_id": null,
	"new_comment_notification_email_template_id": 31,
	"notify_commenters_on_new_comments": true,
	"new_comment_admin_notification_email_template_id": 32
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/blogs/{id}/{nested_resource}`.

### categories

```shell
GET /api/v1/blogs?expand=categories
```

```shell
GET /api/v1/blogs/{id}/categories
```

```json
{
	...
	"categories": [
		{
			"id": 1,
	    "parent_category_id": 0,
	    "type": "Tag",
	    "description": "",
	    "updated_at": "2014-03-05T08:46:30.627-06:00",
	    "created_at": "2014-03-05T08:46:30.627-06:00",
	    "name" "test",
	    "blog_category_path": ""
		},
		...
	],
	...
}
```

### posts

```shell
GET /api/v1/blogs?expand=posts
```

```shell
GET /api/v1/blogs/{id}/posts
```

```json
{
	...
	"posts": [
		{
			"id": 1,
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
			"view_count": 6
		},
		...
	],
	...
}
```