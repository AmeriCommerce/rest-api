order_statuses
==============

```shell
GET /api/v1/order_statuses
```

**Required scope**: `read_orders`, `orders`

Sample Model
------------

```json
{
	"id": 1,
	"name": "Pending Processing",
	"is_open": true,
	"is_declined": false,
	"is_cancelled": false,
	"is_shipped": false,
	"color": "#A4E065",
	"email_template_id": null,
	"updated_at": "2014-02-18T13:36:58.357-06:00",
	"created_at": "2014-02-18T13:36:58.357-06:00",
	"is_fully_refunded": false,
	"is_partially_refunded": false,
	"is_quote_status": false
}
```