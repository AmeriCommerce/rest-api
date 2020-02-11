AmeriCommerce API Authentication
=========================================

All AmeriCommerce API requests require an access token. The purpose of this guide is to give instructions on the ways to obtain one and how to refresh expired tokens.

If your app is mostly just a service app and does not really interact with a user in any way, you can use the admin console to generate a token (more information below).

Getting an Access Token
-----------------------

These instructions make use of digests and assume you know how to generate one (SHA256 in particular). You will need your application's ID and secret from the admin console before you proceed.

### OAuth 2

1. Redirect the user to `https://[mystorename.com]/api/oauth` with the following query string parameters:
  * `client_id` - The App ID given to you in the admin console when you set up the application.
  * `scope` - The permissions that this access token will need. (See [Scopes](https://github.com/AmeriCommerce/rest-api/blob/master/scopes.md) for specifics.)
  * `redirect_uri` - The callback URL that will be returned to after the user has authorized the application.

2. The user will be asked to login with their admin console credentials.

3. After login, the user will be prompted to grant the app access on their behalf.

4. The user will be redirected back to the `redirect_url` that you provided on the initial request with the following query string parameters.
  * `auth_id` - An identifier to represent the handshake.
  * `code` - A verification code.

5. Generate a signature by concatenating the app's secret, `code`, `client_id`, `scope`, and `redirect_uri` (converted to all lowercase), then computing a SHA256 digest of the concatenated string. The digest should be in hex format. **Take extra care here that the `redirect_uri` matches the original `redirect_uri` precisely (before conversion to lowercase), or this will fail.**

6. Send a POST request to `https://[mystorename.com]/api/oauth/access_token` with the following information in the request body (the `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `client_id` - The App ID used to start this process.
  * `auth_id` - The handshake reference given to you when the user returned to your application.
  * `signature` - The signature you generated above: `SHA256(secret + code + client_id + scope + redirect_uri)`.

7. Read back the response from the POST request. If all goes well it should contain an `access_token` and `refresh_token`. That `access_token` can now be used to make requests against the API.

### Generating a Token from the Admin Console

Navigate to the application list at **Tools** > **Apps & Addons** > **API Apps & Integrations**. Next to the app you need a token for, click the *Tokens* icon (second icon from the left that looks like a person). This will open the list of all access tokens that belong to this application. On this screen you can click *New* to open another dialog that presents you with a list of available scopes for the new token. Select the ones you need, then click *Save*.

Once the overlay closes and you see the *Saved successfully* message, your new token should be at the very top of the list. Click the magnifying glass next to it to view the details about that token, including the actual token string that you need to pass in. Tokens created in this way are non-expiring by default so make sure these are protected.

These tokens can be revoked at any time by returning to this screen.

Refreshing Tokens
-----------------

By refreshing a token you are requesting a new access token using the same scope as a previous one without having to grant permissions again (as that part has already been done). Refresh tokens are long living and can be used multiple times.

1. Generate a signature by concatenating the app's secret, the `refresh_token`, and the `app_id`, then calculating the SHA256 of the concatenated string. To summarize: `SHA256(secret + refresh_token + client_id)`.

2. Send a POST request to `https://[mystorename.com]/api/oauth/refresh` with the following information in the request body (the request's `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `client_id` - The App ID.
  * `refresh_token` - The `refresh_token`.
  * `signature` - The signature generated in step 1.

3. Read back the response. If all goes well it should contain the following information:
  * `access_token` - A new `access_token` to use for API requests.
  * `refresh_token` - For use when this `access_token` expires.
  * `expires` - The expiration of the new token.

Error Handling
--------------

There are two error formats that you may encounter when trying to obtain an access token.

In the web flow specifically, in the event there is an error on the OAuth initialization or due to user permissions, the user will be redirected back to the `redirect_url` with three additional query string parameters:

* `error` - The type of error that occured.
* `error_reason` - The reason the error occured.
* `error_description` - A longer description of the error.

During the desktop flow or during token negotiation, errors are sent back on the response with a HTTP status code. The `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded` depending on what the `Content-Type` of the original request was.