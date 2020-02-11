Query Syntax
============

The query syntax is available on every resource root (i.e. `/api/v1/products`). It allows for more advanced filtering of the data returned. All field names (with the exception of nested resources) are available as query string parameters for this functionality. It can be combined with the other parameters that each endpoint supports.

The general format of a query syntax parameter is as follows:

```shell
/api/v1/resource/field_name=op:value
```

* `field_name` - The name of the field that will be compared against.

* `op` - (Optional) The [comparison operator](#comparison-operator) to use when comparing the specified value to the field. Defaults to **eq**.

* `value` - The value being checked for. (Read [here](https://github.com/AmeriCommerce/rest-api/blob/master/datetimes.md) for additional information about using datetimes for this.)

Samples:

```shell
/api/v1/products?item_name=test
```

```shell
/api/v1/orders?ordered_at=gt:2012-12-08T06:00:00.0Z&fields=id,customer_id,grand_total
```

```shell
/api/v1/categories?parent_category_id=14&count=10&page=2
```

Comparison Operators
--------------------

###### eq

This is the default if no operator is specified. Returns results where a field is *equal to* the supplied value.

```shell
/api/v1/products?item_name=test
```

```shell
/api/v1/products?item_name=eq:test
```

###### not

Returns results where a field is *not equal to* the supplied value.

```shell
/api/v1/products?item_name=not:test
```

###### like

Returns results where a field *contains* the supplied value.

```shell
/api/v1/products?item_name=like:test
```

###### gt

Returns results where a field is *greater than* the supplied value.

```shell
/api/v1/products?price=gt:5.00
```

###### gte

Returns results where a field is *greater than or equal to* the supplied value.

```shell
/api/v1/products?price=gte:5.00
```

###### lt

Returns results where a field is *less than* the supplied value.

```shell
/api/v1/products?price=lt:25.00
```

###### lte

Returns results where a field is *less than or equal to* the supplied value.

```shell
/api/v1/products?price=lte:25.00
```

Conjunction Operators
---------------------

Complex queries using parentheses are not supported. The conjunctions we do support will be evaluated in the standard order of operations.

###### AND

The default when multiple fields are specified in a query. Can also be used to specify multiple comparison values for a single field.

```shell
/api/v1/products?item_name=test&price=gt:5.00
```

```shell
/api/v1/products?price=gt:5.00+AND+lte:25.00
```

###### OR

Can prefix the first operator, in which it overrides the default `AND` behavior and uses `OR` instead. It can also be used to specify multiple comparison values for a single field.

```shell
/api/v1/products?weight=OR+gt:3.5&length=gt:12
```

```shell
/api/v1/products?item_name=like:doge+OR+like:wow
```
