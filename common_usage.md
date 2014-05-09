Common Usage
============

Most resources in the AmeriCommerce API support the same set of use cases and have similar response formats for each of them.

GET
---

### Response format

The standard GET requests supported by this API will return results in one of two formats. The results will either be in a single JSON object, or a list result that serves as a wrapper around an array of individual results.

A single object result will just be the JSON for the object:

```shell
{
	"id": 1,
	"item_name": "Item 1",
	"item_number": "item-1",
	...
}
```

While a list result will contain some metadata about the list before the array of results:

```shell
{
	"total_count": 1234,
	"next_page": "https://[mystorename.com]/api/v1/products?page=2",
	"products": [
		{
			"id": 1,
			"item_name": "Item 1",
			...
		},
		{
			"id": 2,
			"item_name": "Item 2",
			...
		},
		...
	]
}
```

There's only a few metadata fields possible on the list result:

* `total_count` - The total number of items possible (not displayed).

* `next_page` - The URI for the next page of results, if it exists.

* `previous_page` - The URI for the previous page of results, if it exists.

### Requesting data

#### List of resources

Fetches a list of resources. Without any additional parameters this will return a paged list that defaults to 100 items per page.

```shell
GET /api/v1/{resource_name}
```

This resource endpoint supports the following parameters:

* `page` - The page of results to display. If this number is out of bounds, the request will return a `404 Not Found`.

* `count` - The number of results to display per page.

* `expand` - A comma-separated list that specifies the nested resources to fill before the result is returned.

* `sort` - A comma-separated list that specifies the sort order for the list of results. A negative sign in front of a field name sorts by that field in decending order.
	* `sort=price,item_name` - Sort by `price` ascending, then by `item_name` ascending
	* `sort=-price,item_name` - Sort by `price` descending, then by `item_name` ascending

* `fields` - A comma-separated list that specifies the particular fields that should be on each resource in the result. If the field is a nested resource, that nested resource will automatically be filled as if it were specified with the `expand` parameter.

This resource endpoint also supports the [query syntax](query_syntax.md) for more selective results.

#### Single resource

Fetches a single resource by its identifier. If the resource does not exist, this method will return a `404 Not Found`.

```shell
GET /api/v1/{resource_name}/{id}
```

This resource endpoint supports the following parameters:

* `expand` - A comma-separated list that specifies the nested resources to fill before the result is returned.

* `fields` - A comma-separated list that specifies the particular fields that should be on the resource. If the field is a nested resource, that nested resource will automatically be filled as if it were specified with the `expand` parameter.

#### Single resource with all nested resources populated

Fetches a single resource by its identifier with all of the nested resources already populated. If the resource does not exist, this method will return a `404 Not Found`.

```shell
GET /api/v1/{resource_name}/{id}/filled
```

This resource endpoint supports the following parameters:

* `fields` - A comma-separated list that specifies the particular fields that should be on the resource.

#### Nested resource list only

Returns the contents of a particular nested resource as a list result, without the rest of the parent object. If the resource or nested resource does not exist, this method will return a `404 Not Found`.

```shell
GET /api/v1/{resource_name}/{id}/{nested_resource_name}
```

This resource endpoint supports the following parameters:

* `sort` - A comma-separated list that specifies the sort order for the list of results. A negative sign in front of a field name sorts by that field in decending order.
	* `sort=price,item_name` - Sort by `price` ascending, then by `item_name` ascending
	* `sort=-price,item_name` - Sort by `price` descending, then by `item_name` ascending

* `fields` - A comma-separated list that specifies the particular fields that should be on the resource.

#### Multiple resources by identifier

Returns a list result of one or more particular resources as specified by their identifiers.

```shell
GET /api/v1/{resource_name}/select_many?ids={ids}
```

This resource endpoint supports the following parameters:

* `ids` - Required. A comma-separated list that specifies the resources to return. If this is not specified, the request will respond with `400 Bad Request`.

* `expand` - A comma-separated list that specifies the nested resources to fill before the result is returned.

* `sort` - A comma-separated list that specifies the sort order for the list of results. A negative sign in front of a field name sorts by that field in decending order.
	* `sort=price,item_name` - Sort by `price` ascending, then by `item_name` ascending
	* `sort=-price,item_name` - Sort by `price` descending, then by `item_name` ascending

* `fields` - A comma-separated list that specifies the particular fields that should be on the resource. If the field is a nested resource, that nested resource will automatically be filled as if it were specified with the `expand` parameter.

POST
----

Creates or updates a resource. If the request body contains the resource's identifier and that resource already exists, the fields passed in on the request will be applied to the existing resource. Otherwise, a new resource will be created.

If a new resource was created, this method will return a `201 Created` status and the body will contain the newly created resource. If an existing resource was updated, the response will be `200 OK` and the body will contain the updated resource.

```shell
POST /api/v1/{resource_name}
```

PUT
---

Updates an existing resource. Only the fields passed in on the request body are applied to the existing resource. On success, this method returns a `200 OK` and the body contains the content of the updated resource. If the resource is not found it will return a `404 Not Found`.

```shell
PUT /api/v1/{resource_name}/{id}
```

DELETE
------

Deletes an existing resource. On success, this method returns a `204 No Content`. If the resource is not found it will return a `404 Not Found`.

```shell
DELETE /api/v1/{resource_name}/{id}
```