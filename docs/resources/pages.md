pages
=====

```shell
GET /api/v1/pages
```

**Required scope**: `read_content`, `content`

Sample Model
------------

```json
{
	"id": 1,
	"title": "About Us",
	"keywords": "about",
	"description": "",
	"content": "<h1>wow</h1><p>such bio, so boring</p>",
	"is_hidden": true,
	"store_id": 1,
	"external_url": "",
	"is_content_only": false,
	"url_rewrite": "/about",
	"updated_at": "2013-10-07T14:16:19.163-05:00",
	"created_at": "2013-10-07T14:16:19.163-05:00",
	"is_secure": false,
	"is_login_required": false,
        "head_tags": ""
}
```