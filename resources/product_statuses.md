product_statuses
================

```shell
GET /api/v1/product_statuses
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 1,
	"name": "In Stock",
	"time_frame": "1-2 Business Days",
	"is_unavailable": false,
	"is_hidden": false,
	"is_back_ordered": false,
	"show_quantity": false,
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00"
}
```