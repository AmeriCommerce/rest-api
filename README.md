The AmeriCommerce API
==============================

The AmeriCommerce API is a REST-style API designed to be a replacement for the legacy SOAP API. While there are no current plans to discontinue the SOAP API, it is recommended that all integrations be converted to use the new API. The new API uses JSON and includes an OAuth 2 authentication mechanism. It is **HTTPS only**.

Setup
-----

To use the API it is assumed that you already have an AmeriCommerce account and access to the admin console. From the admin console you can set up a *custom application*, which is necessary for using the API. To do this, browse to **Tools** > **Apps & Addons** > **API Apps & Integrations** in the admin console. Click the *New* button and fill out the details for your new application. Upon hitting *Save* you will see the *App ID* and *App Secret* displayed on the screen. You will need these for the OAuth process, so it is suggested you make a note of them or at least where to find them.

Making Requests
---------------

All API URLs start with `https://[mystorename.com]/api/v1/`, where `[mystorename.com]` is the domain name of your AmeriCommerce store. All requests require an access token, which can be obtained either through the OAuth 2 process or the admin console (there is one exception, as noted at the end of this section). The access token is passed in as a special header called `X-AC-Auth-Token`.

In curl, a simple request for the product list would look like this:

```shell
curl -H 'X-AC-Auth-Token: [MyAccessToken]' https://[mystorename.com]/api/v1/products.json
```

In this example, `[MyAccessToken]` would be replaced with the actual access token you obtained from the site. Similarly, a request to create a product could look like this. Take note of the `Content-Type` and request body here:

```shell
curl -H 'Content-Type: application/json' \
  -H 'X-AC-Auth-Token: [MyAccessToken]' \
  -d '{ \
    "item_name": "My test product", \
    "item_number": "mytestproduct", \
    "product_status_id": 1, \
    "primary_category_id": 1
  }' \
  https://[mystorename.com]/api/v1/products.json
```

While logged into the admin console of your site, you can view the results of any GET requests from your browser, assuming you have access to the admin area in question. Since your session is already authenticated, you do not need the access token for this.

Authentication
--------------

For convenience to developers writing private integrations that only ever use a single user or run headless, Spark Pay provides a way to create a non-expiring access token from the admin console. There are certain limitations to this type of token, such as not being able to access some types of encrypted data.

The other way to obtain access tokens is via OAuth 2. This is the more secure way to integrate an application with the API and it enforces token expiration. Additionally, if the app is acting on the behalf of particular users, OAuth is a requirement, as the user will then be able to sign in with their admin credentials and use the app just like they would use the admin console.

You can find more information about authentication in the [guide](authentication.md).

The Format
----------

All data serialization is done with JSON. For endpoints that return lists, there is a list metadata object wrapping the array of results. The list metadata gives you information such as paging and total number of results. For properties we use `snake_case`. Datetime objects are expressed in [ISO 8601 format](datetimes.md).

Caching
-------

Most responses in the API are cached on the server, and the appropriate HTTP headers are set when this happens. Typically this will only be on `GET` requests. The response will contain the headers `Last-Modified` and `Expires`, as well as the `Cache-Control` header. It is strongly encouraged to obey these headers when making requests to the API. If you must have up-to-the-second data at all times, the cache can be revalidated on demand by including the header `Cache-Control: no-cache` on your request.

Rate Limiting
-------------

We enforce a rate limit for how many requests an application and/or token can make in a designated period of time. There are two types of REST API applications: installed and custom.  Installed apps are those that are available to be installed directly from the Spark Pay app store or a 3rd party integration app. Custom apps are those that you create manually for a specific store.

Installed apps are subject to the max rate limit of 50 calls per 10 second window, regardless of your plan level.  All installed apps for a particular store combine toward this one overall limit. Custom apps are subject to a separate rate limit that will vary based on your plan level.  The maxium rate limit for custom apps is also 50 calls per 10 second window.  The rate limit for custom apps will scale up as your plan level increases.

All responses from the API include the header `X-AC-Call-Limit` which includes the number of calls made against that store and the total number of calls allowed. This currently resets every 10 seconds. If the limit is exceeded, the API will return the response `429 - Too Many Requests` and will include an additional header `Retry-After`. The `Retry-After` header indicates what time the counter will reset and requests can resume.

Support
-------

All API support for AmeriCommerce is handled through the support portal located at [http://support.americommerce.com/hc/en-us](http://support.americommerce.com/hc/en-us). Please submit a ticket there if you have an issue with the API itself or the documentation you find here.
