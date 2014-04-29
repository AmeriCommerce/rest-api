AmeriCommerce API Authentication
================================

All AmeriCommerce API requests require an access token. The purpose of this guide is to give instructions on the ways to obtain one, how to use security scopes, and how to refresh expired access tokens.

OAuth 2
-------

These instructions make use of digests and assume you know how to generate one (SHA256 in particular). You will need your application's ID and secret from the admin console before you proceed.

### Web Application

1. Redirect the user to `https://[mystorename.com]/api/oauth` with the following query string parameters:
  * `app_id` - The App ID given to you in the admin console when you set up the application.
  * `scope` - The permissions that this access token will need.
  * `redirect_url` - The URL that will be returned to after the user has authorized the application.

2. The user will be asked to login with their admin console credentials.

3. After login, the user will be prompted to grant the app access on their behalf.

4. The user will be redirected back to the `redirect_url` that you provided on the initial request with the following query string parameters.
  * `ref` - An identifier to represent the handshake.
  * `code` - A verification code.

5. Generate a signature by concatenating the app's secret, `code`, `app_id`, `scope`, and `redirect_url`, then computing a SHA256 digest of the concatenated string. The digest should be in hex format.

6. Send a POST request to `https://[mystorename.com]/api/oauth/access_token` with the following information in the request body (the `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `app_id` - The App ID used to start this process.
  * `ref` - The handshake reference given to you when the user returned to your application.
  * `signature` - The signature you generated above: `SHA256(secret + code + app_id + scope + redirect_url)`.

7. Read back the response from the POST request. If all goes well it should contain an `access_token` and `refresh_token`. That `access_token` can now be used to make requests against the API.

### Desktop Application (applications with a webview)

WIP

### Desktop Application (applications without a webview)

This flow does require obtaining user information up front, but instead of their password you will need their user-specific API key. We will use this information to create a login signature so that the user can be logged in securely and your app doesn't need to know or store their real password. The user-specific API key can be found in the admin console under **Tools** > **Apps & Addons** > **Manage Apps** > *More Actions* menu > *View User Authorization Key*. Click the *Show Key* button on that page and it will be displayed.

A user can regenerate this key at any time so it is suggested that you prompt them for it again should authentication fail.

1. Send a POST request to `https://[mystorename.com]/api/oauth` with the following information in the request body (the request's `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `app_id` - The App ID given to you in the admin console when you set up the application.
  * `scope` - The permissions that this access token will need.
  * `redirect_url` - Can be your domain name or anything else for this flow, we're not performing redirection - just be consistent in all the spots that need it.
  * `username` - the username that the user has provided.
  * `signature` - concatenate the application's secret, the `username`, the user-specific API key, `app_id`, `scope`, and `redirect_url`, then calculate the SHA256 hash of the concatenated string. To summarize: `SHA256(secret + username + key + app_id + scope + redirect_url)`.

2. Read the response to this request, it will be in the same `Content-Type` that you sent in. The response will contain the following information:
  * `ref` - An identifier to represent the handshake.
  * `code` - A verification code.

3. Generate a signature by concatenating the app's secret, the `username`, `code`, `app_id`, `scope`, and `redirect_url`, then calculating the SHA256 hash of the concatenated string. To summarize: `SHA256(secret + username + code + app_id + scope + redirect_url)`.

4. Send another POST request to `https://[mystorename.com]/api/oauth/access_token` with the following information in the request body (the request's `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
  * `app_id` - The App ID used throughout this process.
  * `ref` - The handshake identifier returned from the previous request.
  * `signature` - The signature generated from the previous step.

5. Read back the response from the previous POST request. If all goes well it should contain an `access_token` and `refresh_token`. That `access_token` can now be used to make requests against the API.