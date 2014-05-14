drips
=====

```shell
GET /api/v1/drips
```

Sample Model
------------

```json
{
	"id": 1,
	"name": "test",
	"is_enabled": false
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/drips/{id}/{nested_resource}`.

### members

### events