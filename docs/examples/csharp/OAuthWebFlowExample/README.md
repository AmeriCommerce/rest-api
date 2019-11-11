C# Web Flow Example
===================

This example uses a simple ASP.NET MVC application to give a general overview of how web-based authentication works. 

The `ProductsController` acts as the entry point into the application and makes a basic API request to the resource `/api/v1/products`. On this controller class we have an `OAuth` action filter which will check to see that we have an access token for this user. If we do not, the filter will send the user to the `SessionsController`.

The `SessionsController` performs the authentication steps. The `Index` action redirects the user to the OAuth initialization url on the store, providing a callback URL to return to. The `Callback` action is that callback URL, and at this point the `Callback` action will generate a verification signature, which it will then `POST` to the store. If everything succeeds, this returns an access token (which for the sake of simplicity, is stored on the current session), then the user is redirected back to the resource they originally requested.