cart_items
==========

```shell
GET /api/v1/cart_items
```

**Required scope**: `read_orders`, `orders`

Sample Model
------------

```json
{
  "id": 34,
  "product_id": 4,
  "item_number": "",
  "quantity": 1,
  "price": 200,
  "cost": 0,
  "item_url": "",
  "item_name": "Golf Balls - Titliest",
  "warehouse_id": 0,
  "parent_product_id": null,
  "parent_cart_item_id": null,
  "updated_at": "2013-10-07T11:18:14.823-05:00",
  "created_at": "2013-10-07T11:17:53.867-05:00",
  "cart_id": 3,
  "is_subscription_product": false,
  "variants": [
    {
      "id": 10,
      "description": "Color: 12",
      "variant_group_id": 3
    }
  ],
  "personalizations": null
}
```

Nested Resources
----------------

### child_items

```shell
GET /api/v1/cart_items?expand=child_items
```

```shell
GET /api/v1/carts/{id}/child_items
```

```json
{
  ...
  "child_items": [
    {
      "id": 321,
      "product_id": 62,
      "item_number": "60PY2DR",
      "quantity": 2,
      "price": 2295,
      "cost": 0,
      "item_url": "",
      "item_name": "60PY2DR",
      "warehouse_id": 0,
      "parent_product_id": 4,
      "parent_cart_item_id": 34,
      "updated_at": "2013-10-07T11:18:14.823-05:00",
      "created_at": "2013-10-07T11:18:14.823-05:00",
      "is_subscription_product": false,
      "variants": null,
      "personalizations": null
    },
    ...
  ]
}
```