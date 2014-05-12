Datetime Format
===============

The format for datetimes in this API follows the [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601). This format will work when passed in for the [query syntax](query_syntax.md) as well as on request bodies for POST/PUT requests.

There are a couple of common variations to this format: one with the timezone offset, and one without.

###### UTC

```shell
2014-05-12T00:00:00.0Z
```

###### Local Time

```shell
2014-05-13T06:00:00.000-06:00
```

From Code
---------

###### C#

Libraries like [RestSharp](http://restsharp.org/) and [JSON.NET](http://james.newtonking.com/json) will handle this format for you.

```shell
DateTime.UtcNow.ToString("s")   // NOTE: DateTime.Now.ToString("s") will give local time without the offset
```

```shell
DateTime.Now.ToString("yyyy-MM-dd'T'HH:mm:ss.FFFFFFK")
```