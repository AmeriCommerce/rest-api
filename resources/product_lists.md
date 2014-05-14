product_lists
=============

```shell
GET /api/v1/product_lists
```

Sample Model
------------

```json
{
	"id": 1,
	"name": "Stuff"
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/product_lists/{id}/{nested_resource}`.

### items