sessions
========

This resource is read only (only `GET` actions are available).

```shell
GET /api/v1/sessions
```

**Required scope**: `system`

Sample Model
------------

```json
{
	"id": 1,
	"customer_id": 0,
	"user_id": 1,
	"first_hit_at": "2013-10-01T14:31:32.793-05:00",
	"last_hit_at": "2013-10-01T15:06:19.41-05:00",
	"ip_address": "127.0.0.1",
	"host_name": "",
	"adcode_id": 0,
	"hit_count": 135,
	"visit_count": 135,
	"page_last_visited": "/store/Default.aspx",
	"referer": "",
	"is_abandoned": 0,
	"user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36",
	"cart_id": 63,
	"wish_list_cart_id": 0
}
```