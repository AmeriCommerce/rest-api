blogs
=====

```shell
GET /api/v1/blogs
```

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

### posts