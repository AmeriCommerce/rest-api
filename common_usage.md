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

While logged into the admin console, you can use the examples for any of the `GET` requests from your browser to see what the results look like.

#### List of resources

Fetches a list of resources. Without any additional parameters this will return a paged list. This endpoint also supports the [query syntax](query_syntax.md) for more selective results.

```shell
GET /api/v1/{resource_name}
```

The `{resource_name}` can be any of the root level [resources](resource_list.md).

```shell
GET /api/v1/products
```

This resource endpoint supports the following parameters:

###### page

The page of results to display. By default this is set to **1**. If this number is out of bounds, the request will return a `404 Not Found`.

```shell
GET /api/v1/products?page=2
```

###### count

The number of results to display per page. By default this is set to **100**.

```shell
GET /api/v1/products?count=10
```

###### expand

A comma-separated list that specifies the nested resources to fill before the result is returned.

```shell
GET /api/v1/products?expand=categories,variants
```

###### sort

A comma-separated list that specifies the sort order for the list of results. A negative sign in front of a field name sorts by that field in decending order.

For example, to sort by `price` ascending, the syntax would look like:

```shell
GET /api/v1/products?sort=price
```

For `price` descending instead, it would be:

```shell
GET /api/v1/products?sort=-price
```

And to do `price` descending, followed by `item_name` ascending, it would be:

```shell
GET /api/v1/products?sort=-price,item_name
```

###### fields

A comma-separated list that specifies the particular fields that should be on each resource in the result. If the field is a nested resource, that nested resource will automatically be filled as if it were specified with the `expand` parameter.

```shell
GET /api/v1/products?fields=id,item_name,item_number,price,categories
```

#### Single resource

Fetches a single resource by its identifier. If the resource does not exist, this method will return a `404 Not Found`.

```shell
GET /api/v1/{resource_name}/{id}
```

The `{resource_name}` can be any of the root level [resources](resource_list.md). The `{id}` is expected to be an integer that uniquely identifies a particular resource.

```shell
GET /api/v1/products/1
```

This resource endpoint supports the following parameters:

###### expand

A comma-separated list that specifies the nested resources to fill before the result is returned.

```shell
GET /api/v1/products/1?expand=categories,variants
```

###### fields

A comma-separated list that specifies the particular fields that should be on the resource. If the field is a nested resource, that nested resource will automatically be filled as if it were specified with the `expand` parameter.

```shell
GET /api/v1/products/1?fields=id,item_name,item_number,price,categories
```

#### Single resource with all nested resources populated

Fetches a single resource by its identifier with all of the nested resources already populated. If the resource does not exist, this method will return a `404 Not Found`.

```shell
GET /api/v1/{resource_name}/{id}/filled
```

The `{resource_name}` can be any of the root level [resources](resource_list.md). The `{id}` is expected to be an integer that uniquely identifies a particular resource.

```shell
GET /api/v1/products/1/filled
```

This resource endpoint supports the following parameters:

###### fields

A comma-separated list that specifies the particular fields that should be on the resource.

```shell
GET /api/v1/products/1/filled?fields=id,item_name,item_number,price,categories
```

#### Nested resource list only

Returns the contents of a particular nested resource as a list result, without the rest of the parent object. If the resource or nested resource does not exist, this method will return a `404 Not Found`.

```shell
GET /api/v1/{resource_name}/{id}/{nested_resource_name}
```

The `{resource_name}` can be any of the root level [resources](resource_list.md). The `{id}` is expected to be an integer that uniquely identifies a particular resource. The `{nested_resource_name}` will be any of the collection names also supported by `expand` in other requests.

```shell
GET /api/v1/products/1/variants
```

This resource endpoint supports the following parameters:

###### sort

A comma-separated list that specifies the sort order for the list of results. A negative sign in front of a field name sorts by that field in decending order.

For example, to sort by `sort_order` ascending, the syntax would look like:

```shell
GET /api/v1/products/1/variants?sort=sort_order
```

For `sort_order` descending instead, it would be:

```shell
GET /api/v1/products/1/variants?sort=-sort_order
```

And to do `sort_order` descending, followed by `description` ascending, it would be:

```shell
GET /api/v1/products?sort=-sort_order,description
```

###### fields

A comma-separated list that specifies the particular fields that should be on the resource.

```shell
GET /api/v1/products/1/variants?fields=id,product_id,description
```

#### Multiple resources by identifier

Returns a list result of one or more particular resources as specified by their identifiers.

```shell
GET /api/v1/{resource_name}/select_many?ids={ids}
```

The `{resource_name}` can be any of the root level [resources](resource_list.md). The `{ids}` query string parameter is required for this request and is a comma-separated list of identifiers that you want this resource to return. If the `{ids}` parameter is omitted, this request will respond with `400 Bad Request`.

```shell
GET /api/v1/products/select_many?ids=1,5,9
```

This resource endpoint supports the following additional parameters:

###### expand

A comma-separated list that specifies the nested resources to fill before the result is returned.

```shell
GET /api/v1/products/select_many?ids=1,5,9&expand=categories,variants
```

###### sort

A comma-separated list that specifies the sort order for the list of results. A negative sign in front of a field name sorts by that field in decending order.

```shell
GET /api/v1/products/select_many?ids=1,5,9&sort=price
```

For `price` descending instead, it would be:

```shell
GET /api/v1/products/select_many?ids=1,5,9&sort=-price
```

And to do `price` descending, followed by `item_name` ascending, it would be:

```shell
GET /api/v1/products/select_many?ids=1,5,9&sort=-price,item_name
```

###### fields

A comma-separated list that specifies the particular fields that should be on the resource. If the field is a nested resource, that nested resource will automatically be filled as if it were specified with the `expand` parameter.

```shell
GET /api/v1/products/select_many?ids=1,5,9&fields=id,item_name,item_number,price,categories
```

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