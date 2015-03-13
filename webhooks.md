Webhooks
========

Webhooks are a way to run code on an external server that integrates with events in the AmeriCommerce system. When the conditions are fulfilled, the AmeriCommerce store will make a request out to a URL, and, depending on the webhook, wait for a response.

### Webhook Types

| Event Type | Description | Reply? |
| ---- | ----------- | ------ |
| AuthorizingPayment | Called to authorize a payment | Yes |
| CapturingPayment | Called to capture a payment | Yes |
| GetPrice | Called when calculating price for one or more products | Yes |
| GetProductStatus | Called when checking the status of a product for display | Yes |
| GetTax | Called when calculating tax for a cart | Yes |
| OrderApproved | Called after an order has been marked with an Approved order status | No |
| OrderCanceled | Called after an order has been marked with a Canceled order status | No |
| OrderDeclined | Called after an order has been marked with a Declined order status | No |
| OrderPlaced | Called after a new order has been placed | No |
| PaymentProcessed | Called after a payment has finished processing | No |
| ProductStatusChanged | Called when a product's status has been changed | No |
| ValidateCart | Called when the current cart is being checked for errors | Yes |
| ValidateCheckout | Called when the checkout page is being checked for errors | Yes |

### Subscribing to a Webhook

Webhook subscriptions are accessible via `/api/v1/webhooks`, which works exactly the same as any other API endpoint. The webhook resource consists of the following fields:

 * `event_type` - The webhook type, as shown in the table above
 * `url` - The URL that will be sent a request when the conditions for the event are met
 * `failure_type` - What to do in the event of a failure, options are:
   * `"Ignore"` - Disregard the failure and continue as normal, this is the default
   * `"Error"` - Display an error message to the user
   * `"Fallback"` - Call an alternate URL as indicated by the `fallback_url` field
 * `store_id` - The ID of the store that this webhook applies to, only events on this store will be triggered
 * `cache_length` - How long the response to this webhook request will be cached by the AmeriCommerce servers, options are:
   * `"Short"` - 5 minutes
   * `"Long"` - 30 minutes
   * `"NoCache"` - Do not cache the response
 * `fallback_url` - In the event of a failure, and the `failure_type` is set to `"Fallback"`, this URL will be called next
