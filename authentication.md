AmeriCommerce API Authentication
================================

All AmeriCommerce API requests require an access token. The purpose of this guide is to give instructions on the ways to obtain one and how to refresh expired tokens.

Getting an Access Token
-----------------------

These instructions make use of digests and assume you know how to generate one (SHA256 in particular). You will need your application's ID and secret from the admin console before you proceed.

### Creating Signatures

In the processes below, there are some points where you will be asked to generate a signature. Each time will require slightly different information, but the overall process is the same:

1. Concatenate all of the required information. This always starts with the application's secret.

2. Calculate the SHA256 digest of the concatenated string.

The signature is expected as a hex string when it is sent in on a request.

### Web Application

1. Redirect the user to `https://[mystorename.com]/api/oauth` with the following query string parameters:
  * `app_id` - The App ID given to you in the admin console when you set up the application.
  * `scope` - The permissions that this access token will need. (See [Scopes](scopes.md) for specifics.)
  * `redirect_url` - The URL that will be returned to after the user has authorized the application.

2. The user will be asked to login with their admin console credentials.

3. After login, the user will be prompted to grant the app access on their behalf.

4. The user will be redirected back to the `redirect_url` that you provided on the initial request with the following query string parameters.
  * `auth_id` - An identifier to represent the handshake.
  * `code` - A verification code.

5. Generate a signature by concatenating the app's secret, `code`, `app_id`, `scope`, and `redirect_url` (converted to all lowercase), then computing a SHA256 digest of the concatenated string. The digest should be in hex format. **Take extra care here that the `redirect_url` matches the original `redirect_url` precisely (before conversion to lowercase), or this will fail.**

6. Send a POST request to `https://[mystorename.com]/api/oauth/access_token` with the following information in the request body (the `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `app_id` - The App ID used to start this process.
  * `auth_id` - The handshake reference given to you when the user returned to your application.
  * `signature` - The signature you generated above: `SHA256(secret + code + app_id + scope + redirect_url)`.

7. Read back the response from the POST request. If all goes well it should contain an `access_token` and `refresh_token`. That `access_token` can now be used to make requests against the API.

### Desktop Application

This flow does require obtaining user information up front, but instead of their password you will need their user-specific API key. We will use this information to create a login signature so that the user can be logged in securely and your app doesn't need to know or store their real password. The user-specific API key can be found in the admin console under **Tools** > **Apps & Addons** > **API Apps & Integrations** > *More Actions* menu > *View User Authorization Key*. Click the *Show Key* button on that page and it will be displayed.

A user can regenerate this key at any time so it is suggested that you prompt them for it again should authentication fail.

1. Send a POST request to `https://[mystorename.com]/api/oauth` with the following information in the request body (the request's `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `app_id` - The App ID given to you in the admin console when you set up the application.
  * `scope` - The permissions that this access token will need. (See [Scopes](scopes.md) for specifics.)
  * `redirect_url` - Can be your domain name or anything else for this flow, we're not performing redirection - just be consistent in all the spots that need it.
  * `username` - the username that the user has provided.
  * `signature` - concatenate the application's secret, the `username`, the user-specific API key, `app_id`, `scope`, and `redirect_url`, then calculate the SHA256 hash of the concatenated string. To summarize: `SHA256(secret + username + key + app_id + scope + redirect_url)`.

2. Read the response to this request, it will be in the same `Content-Type` that you sent in. The response will contain the following information:
  * `auth_id` - An identifier to represent the handshake.
  * `code` - A verification code.

3. Generate a signature by concatenating the app's secret, `code`, `app_id`, `scope`, and `redirect_url`, then calculating the SHA256 hash of the concatenated string. To summarize: `SHA256(secret + username + code + app_id + scope + redirect_url)`.

4. Send another POST request to `https://[mystorename.com]/api/oauth/access_token` with the following information in the request body (the request's `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `app_id` - The App ID used throughout this process.
  * `auth_id` - The handshake identifier returned from the previous request.
  * `signature` - The signature generated from the previous step.

5. Read back the response from the previous POST request. If all goes well it should contain an `access_token` and `refresh_token`. That `access_token` can now be used to make requests against the API.

Refreshing Tokens
-----------------

By refreshing a token you are trading in an expired access token for a new one, without having to grant access again (as that part has already been done).

1. Generate a signature by concatenating the app's secret, the previous `access_token`, the `refresh_token`, and the `app_id`, then calculating the SHA256 of the concatenated string. To summarize: `SHA256(secret + access_token + refresh_token + app_id)`.

2. Send a POST request to `https://[mystorename.com]/api/oauth/refresh` with the following information in the request body (the request's `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `app_id` - The App ID used to originally obtain the `access_token`.
  * `access_token` - The original `access_token`.
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