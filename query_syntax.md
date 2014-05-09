Query Syntax
============

The query syntax is available on the default list endpoint of every resource. It allows for more advanced filtering of the data returned. All field names (with the exception of nested resources) are available as query string parameters for this functionality.

The general format of a query syntax parameter is as follows:

```shell
field_name=op:value
```

* `field_name` - The name of the field that will be compared against.

* `op` - (Optional) The [comparison operator](#comparison-operator) to use when comparing the specified value to the field. Defaults to **eq**.

* `value` - The value being checked for.

Comparison Operators
--------------------

### eq

This is the default if no operator is specified. Returns results where a field is *equal to* the supplied value.

```shell
item_name=test
```

```shell
item_name=eq:test
```

### not

Returns results where a field is *not equal to* the supplied value.

```shell
item_name=not:test
```

### like

Returns results where a field *contains* the supplied value.

```shell
item_name=like:test
```

### gt

Returns results where a field is *greater than* the supplied value.

```shell
price=gt:5.00
```

### gte

Returns results where a field is *greater than or equal to* the supplied value.

```shell
price=gte:5.00
```

### lt

Returns results where a field is *less than* the supplied value.

```shell
price=lt:25.00
```

### lte

Returns results where a field is *less than or equal to* the supplied value.

```shell
price=lte:25.00
```

Conjunction Operators
---------------------

### AND

The default when multiple fields are specified in a query. Can also be used to specify multiple comparison values for a single field.

```shell
item_name=test&price=gt:5.00
```

```shell
price=gt:5.00+AND+lte:25.00
```

### OR

Can prefix the first operator, in which it overrides the default `AND` behavior and uses `OR` instead. It can also be used to specify multiple comparison values for a single field.

```shell
item_name=like:test&price=OR+lte:25.00
```

```shell
item_name=like:doge+OR+like:wow
```

Additional Notes
----------------

Datetimes are possible with this syntax, but they must be specified in a particular format. The format we support for this is [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601).