[//]: # (Zendesk: 202836780)
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

###### CSharp

Libraries like [RestSharp](http://restsharp.org/) and [JSON.NET](http://james.newtonking.com/json) will handle this format for you.

```csharp
DateTime.UtcNow.ToString("s")   // NOTE: DateTime.Now.ToString("s") will give local time without the offset
```

```csharp
DateTime.Now.ToString("yyyy-MM-dd'T'HH:mm:ss.FFFFFFK")
```

###### Python

```python
>>> from datetime import datetime
>>> datetime.utcnow().isoformat()
'2014-05-12T14:51:02.206277'
```

###### Ruby

```irb
irb(main):001:0> require 'time'
=> true
irb(main):002:0> Time.now.iso8601
=> "2014-05-12T09:47:09-05:00"
irb(main):003:0> Time.now.utc.iso8601
=> "2014-05-12T14:47:16Z"
```

###### node.js

```js
> var date = new Date();
undefined
> date.toISOString();
'2014-05-12T14:53:34.524Z'
```