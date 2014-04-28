AmeriCommerce API Authentication
================================

All AmeriCommerce API requests require an access token. The purpose of this guide is to give instructions on the ways to obtain one, how to use security scopes, and how to refresh expired access tokens.

OAuth 2
-------

These instructions make use of digests and assume you know how to generate one (SHA256 in particular).

### Web Application

1. Redirect the user to `https://[mystorename.com]/api/oauth` with the following query string parameters:
--* `app_id` - The App ID given to you in the admin console when you set up the application.
--* `scope` - The permissions that this access token will need.
--* `redirect_url` - The URL that will be returned to after the user has authorized the application.

2. The user will be asked to login with their admin console credentials.

3. After login, the user will be prompted to grant the app access on their behalf.

4. The user will be redirected back to the `redirect_url` that you provided on the initial request with the following query string parameters.
--* `ref` - An identifier to represent the handshake.
--* `code` - A verification code.

5. Generate a signature by concatenating the app's secret, `code`, `app_id`, `scope`, and `redirect_url`, then computing a SHA256 digest of the concatenated string. The digest should be in hex format.

6. Send a POST request to `https://[mystorename.com]/api/oauth/access_token` with the following information in the request body (the `Content-Type` can be either `application/json` or `application/x-www-form-urlencoded`):
--* `app_id` - The App ID used to start this process.
--* `ref` - The handshake reference given to you when the user returned to your application.
--* `signature` - The signature you generated above (`SHA256(secret + code + app_id + scope + redirect_url)`).

7. Read back the response from the POST request. If all goes well it should contain an `access_token` and `refresh_token`. That `access_token` can now be used to make requests against the API.