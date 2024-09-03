blacklisted_ips
=================

```shell
GET /api/v1/blacklisted_ips
```

**Required scope**: `settings`

Sample Model
------------

```json
{
	"id": 1,
    "ip_address": "12.34.56.78",
    "hit_count": null,
    "last_hit_at": null,
    "user_agent": "",
    "description": ""
}
```