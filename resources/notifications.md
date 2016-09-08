notifications
===============

```shell
GET /api/v1/notifications
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
  "notification_id": 1,
  "product_id": 79,
  "email_address": "notificationsample@capitalone.com",
  "customer_id": 30,
  "notification_frequency_type": "Once",
  "store_id": 3,
  "variant_inventory_id": null
}
```
