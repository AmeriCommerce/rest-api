Webhooks
========

Webhooks are a way to run code on an external server that integrates with events in the Spark Pay Online Store. When the conditions are fulfilled, the Spark Pay Online Store will make a request out to a URL, and, depending on the webhook, wait for a response.

In the case of events that expect responses, the timeout is intentionally short (3 seconds), since any delay can potentially be disrupting to users of the store. It is highly recommended that your service return results as quickly as possible.

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
| OrderShipped | Called after an order has been marked with a Shipped order status | No |
| PaymentProcessed | Called after a payment has finished processing | No |
| ProductStatusChanged | Called when a product's status has been changed | No |
| ValidateCart | Called when the current cart is being checked for errors | Yes |
| ValidateCheckout | Called when the checkout page is being checked for errors | Yes |

### Subscribing to a Webhook

Webhook subscriptions are accessible via `/api/v1/webhooks`, which works exactly the same as any other API endpoint. The webhook resource consists of the following fields:

 * `event_type` - The webhook type, as shown in the table above.
 * `url` - The URL that will be sent a request when the conditions for the event are met.
 * `failure_type` - What to do in the event of a failure, options are:
   * `"Ignore"` - Disregard the failure and continue as normal, this is the default.
   * `"Error"` - Display an error message to the user.
   * `"Fallback"` - Call an alternate URL as indicated by the `fallback_url` field.
 * `store_id` - The ID of the store that this webhook applies to, only events on this store will be triggered.
 * `cache_length` - How long the response to this webhook request will be cached by the Spark Pay Online Store servers, options are:
   * `"Short"` - 5 minutes
   * `"Long"` - 30 minutes
   * `"NoCache"` - Do not cache the response.
 * `fallback_url` - In the event of a failure, and the `failure_type` is set to `"Fallback"`, this URL will be called next.

### Detailed Information

#### AuthorizingPayment

###### Request

The request contains the following:

 * `order_payment` - Object. An order payment model, as shown on the [`order_payments`](resources/order_payments.md) resource. 

###### Response

The response to this webhook is expected to contain:

 * `approved` - Boolean. Was this authorization approved or not.
 * `declined` - Boolean. Was this authorization declined.
 * `authorization_code` - String. Set if an authorization code was returned from the processor.
 * `transaction_id` - String. Set if a transaction ID was returned from the processor.
 * `avs_code` - String. Set if the processor uses AVS as a verification mechanism and returns this information.
 * `reject_reason` - String. Reason for declining the authorization.
 * `notes` - String. Any additional information about this authorization.
 * `outstanding_balance` - Decimal. Remaining balance in the event that this authorization did not cover the full balance.

---

#### CapturingPayment

###### Request

The request contains the following:

 * `order_payment` - Object. An order payment model, as shown on the [`order_payments`](resources/order_payments.md) resource. 

###### Response

The response to this webhook is expected to contain:

* `approved` - Boolean. Was this capture approved or not.
* `declined` - Boolean. Was this capture declined.
* `authorization_code` - String. Set if an authorization code was returned from the processor.
* `transaction_id` - String. Set if a transaction ID was returned from the processor.
* `avs_code` - String. Set if the processor uses AVS as a verification mechanism and returns this information.
* `reject_reason` - String. Reason for declining the authorization.
* `notes` - String. Any additional information about this authorization.
* `outstanding_balance` - Decimal. Remaining balance in the event that this capture did not cover the full balance.

---

#### GetPrice

###### Request

The request contains the following:

 * `items` - Array. Contains summarized product information indicating the items we need pricing information for:
   * `item_number` - String. The product's item number.
   * `quantity` - Integer. The number of products we need pricing for.
   * `variant_ids` - Array containing the integer IDs of the [`product_variants`](resources/product_variants.md) selected, if any exist.
   * `variant_inventory_id` - Integer. ID of the corresponding [`variant_inventory`](resources/variant_inventory.md) record.
 * `customer_type_id` - The [`customer_type`](resources/customer_types.md) in effect at the time of the request.

###### Response

The response to this webhook is expected to contain:

 * `prices` - Array. Consists of objects with the following information:
   * `item_number` - String. This should match up with one of the request's item numbers.
   * `price` - Decimal. The calculated final price for the item.
   * `cost` - Decimal. The item's cost to the seller.
   * `retail` - Decimal. The retail price for the item.
   * `pre_sale_cost` - Decimal. The cost without any sale discount applied.
   * `pre_sale_price` - Decimal. The price without any sale discount applied.

---

#### GetProductStatus

###### Request

The request contains the following:

* `items` - Array. Contains summarized information for the products we need status information for:
  * `product_id` - Integer. The ID of the [`product`](resources/products.md).
  * `variant_inventory_id` - Integer. The ID of the applicable [`variant_inventory`](resources/variant_inventory.md) record, if it exists.
  * `product_status_id` - Integer. The ID of the current [`product_status`](resources/product_statuses.md).
  * `product` - Object. Product model as shown on the [`products`](resources/products.md) resource.
  * `variant_inventory` - Object. Variant inventory model as shown on the [`variant_inventory`](resources/variant_inventory.md) resource.
  * `product_status` - Object. Product status model as shown on the [`product_statuses`](resources/product_statuses.md) resource.
  * `inventory` - Integer. Current stock of this item.
  * `item_number` - String. The product's item number.
  * `manufacturer_item_number` - String. The product's manufacturer item number.

###### Response

The response to this webhook is expected to contain:

* `items` - Array. Contains status information that corresponds to the data sent from the webhook request:
  * `product_id` - Integer. The ID of the [`product`](resources/products.md) that this data corresponds to.
  * `variant_inventory_id` - Integer. The ID of the applicable [`variant_inventory`](resources/variant_inventory.md) record, if it exists.
  * `inventory` - Integer. Current stock of this item.
  * `status_display_text` - String. The text to display for this item's status on frontend pages.
  * `product_status_id` - Integer. The ID of the [`product_status`](resources/product_statuses.md) to set for this product.
  * `is_unavailable` - Boolean. Indicates that the product is not available for purchase.
  * `is_hidden` - Boolean. Indicates that this product should be hidden from customer view.
  * `is_back_ordered` - Boolean. Indicates that this product is currently backordered.

---

#### GetTax

###### Request

The request contains the following:

* `items` - Array. Contains summarized information for the items in the cart that tax is being calculated for:
  * `cart_item_id` - Integer. The ID of the [`cart_item`](resources/cart_items.md).
  * `item_number` - String. The product's item number.
  * `item_name` - String. The product's name.
  * `manufacturer_item_number` - String. The product's manufacturer item number.
  * `price` - Decimal. The price of the item in the cart.
  * `discounted_price` - Decimal. The price of the item in the cart with discounts applied.
  * `quantity` - Integer. How many of this item are in the cart.
  * `is_tax_exempt` - Boolean. Is the item flagged as being tax exempt.
  * `tax_code` - String. Tax exempt code, if it exists.
  * `line_item_subtotal` - Decimal. Price multiplied by quantity.
  * `origin_address` - Object. The [`warehouse`](resources/warehouses.md) that the item is being shipped from.
  * `destination_address` - Object. The [`address`](resources/addresses.md) that the item is being shipped to.
* `shipping_total` - Decimal. The amount calculated for shipping on the current cart.
* `handling_total` - Decimal. The amount calculated for handling on the current cart.

###### Response

The response to this webhook is expected to contain:

* `items` - Array. Contains information about the tax amounts for each item:
  * `cart_item_id` - Integer. This should match a `cart_item_id` on the incoming request. Specifies which cart item this tax amount is for.
  * `tax_amount` - Decimal. The calculated tax amount for this cart item.
* `shipping_tax_amount` - Decimal. The calculated tax amount for shipping.
* `handling_tax_amount` - Decimal. The calculated tax amount for handling.

---

#### OrderApproved

###### Request

The request contains the following:

* `order` - Object. An order model, as shown on the [`orders`](resources/orders.md) resource.

---

#### OrderCanceled

###### Request

The request contains the following:

* `order` - Object. An order model, as shown on the [`orders`](resources/orders.md) resource.

---

#### OrderDeclined

###### Request

The request contains the following:

* `order` - Object. An order model, as shown on the [`orders`](resources/orders.md) resource.

---

#### OrderPlaced

###### Request

The request contains the following:

* `order` - Object. An order model, as shown on the [`orders`](resources/orders.md) resource.

---

#### OrderShipped

###### Request

The request contains the following:

* `order` - Object. An order model, as shown on the [`orders`](resources/orders.md) resource.

---

#### PaymentProcessed

###### Request

The request contains the following:

 * `order_payment` - Object. An order payment model, as shown on the [`order_payments`](resources/order_payments.md) resource. 

---

#### ProductStatusChanged

###### Request

The request contains the following:

* `item` - Object. A summary of data about the item and its inventory information
  * `product_id` - Integer. The ID of the [`product`](resources/products.md).
  * `variant_inventory_id` - Integer. The ID of the applicable [`variant_inventory`](resources/variant_inventory.md) record, if it exists.
  * `product_status_id` - Integer. The ID of the current [`product_status`](resources/product_statuses.md).
  * `product` - Object. Product model as shown on the [`products`](resources/products.md) resource.
  * `variant_inventory` - Object. Variant inventory model as shown on the [`variant_inventory`](resources/variant_inventory.md) resource.
  * `product_status` - Object. Product status model as shown on the [`product_statuses`](resources/product_statuses.md) resource.
  * `inventory` - Integer. Current stock of this item.
  * `item_number` - String. The product's item number.
  * `manufacturer_item_number` - String. The product's manufacturer item number.

---

#### ValidateCart

###### Request

The request contains the following:

* `cart` - Object. A cart model as it appears on the [`carts`](resources/carts.md) resource.

###### Response

The response to this webhook is expected to contain:

* `validation_messages` - Array. Consists of validation messages (strings) to display to the user.

---

#### ValidateCheckout

###### Request

The request contains the following:

* `customer` - Object. A customer model as it appears on the [`customers`](resources/customers.md) resource.
* `billing_address` - Object. An address model as it appears on the [`addresses`](resources/addresses.md) resource.
* `shipping_address` - Object. An address model as it appears on the [`addresses`](resources/addresses.md) resource.
* `cart` - Object. A cart model as it appears on the [`carts`](resources/carts.md) resource.
* `order_custom_fields` - Array. Objects that represent the information entered for order custom fields on the checkout page:
  * `name` - String. The name of the custom field.
  * `value` - String. The value entered for the custom field.
* `is_gift` - Boolean. True if the customer checked "Is a Gift" at checkout.
* `gift_message` - String. The gift message entered by the customer.
* `order_comments` - String. Any order comments entered by the customer.
* `shipping_methods` - Array. Consists of the names of one or more shipping methods selected at checkout.
* `payment_methods` - Array. Consists of objects containing information about the payments applied:
  * `name` - String. Name of the payment method.
  * `amount` - Decimal. Amount of the payment.

###### Response

The response to this webhook is expected to contain:

* `validation_messages` - Array. Consists of validation messages (strings) to display to the user.

---

#### GetDiscount

###### Request

The request contains the following:

* `ad_code` - String. [`ad code`](https://support.sparkpay.com/hc/en-us/articles/201903360-HOWTO-Setup-Campaign-AdCodes) set on the current session.
* `billing_address` - Object.  An address model as it appears on the [`addresses`](resources/addresses.md) resource.
* `campaign_code` - String. [`campaign code`]('resources/coupon_codes') set on the cart. 
* `cart_id` - Integer. ID of the current [`cart`]('resources/carts')
* `customer_type` - String. The [`customer type`]('resources/customer_types.md') name
* `customer_type_id` - Integer. ID of the [`customer type`](resources/customer_types.md)
* `destination_address` - Object.  An address model as it appears on the [`addresses`](resources/addresses.md) resource. 
* `is_region_set` - Boolean. Is a specific region set
* `items` - Array of Objects 
    * `cart_item_id` - Integer. ID of the [`cart item`](resources/cart_items.md)
    * `category_id` - Array of Integers. List of [`category`](resources/categories.md) ids this item belongs to.
    * `custom_fields` - Object
        * `name` - String
        * `value` - String
    * `destination_address` - Object. An address model as it appears on the [`addresses`](resources/addresses.md) resource.
    * `is_subscription_item` - Boolean. Is this a subscription item?
    * `item_number` - String. Item Number as it appears on the [`product`](resources/products.md) resource.
    * `manufacturer_id` - Integer. ID of the [`manufacturer`](resources/manufacturers.md)
    * `origin_address` - Object. An address model as it appears on the [`addresses`](resources/addresses.md) resource.
    * `parent_product_id` - Integer. ID of the [`parent product`](resources/products.md)
    * `price` - Decimal. Unit price of the item.
    * `product_id` - Integer. ID of the [`product`](resources/products.md)
    * `product_list_id` - Array of Integer. IDs of the product lists this product belongs to.
    * `quantity` - Integer. Quantity
    * `shipping_classification_code` - String. Breakout shipping classification code
    * `variants` - Array of Object.
            * `group` - String. Variant group
            * `value` - String. Variant name
* `shipping_method_list` - Object.
    * `classification_code` - String. Breakout shipping classification code
    * `delivery_date` - String. Estimated delivery date
    * `ship_method` - String. Selected shipping method
    * `shipping_method_name` - String. Selected shipping method name
* `shipping_region_id` - Integer. ID of the [`shipping region`](resources/regions.md)
* `shipping_total` - Decimal. Shipping Total
* `store_id` - Integer. ID of the [`store`](resources/stores.md)
* `subscription_subtotal` - Decimal. Subtotal of the subscription items
* `tax_region_id` - Integer. ID of the [`tax region`](resources/regions.md)
* `total_weight` - Decimal. Total weight of the items in the cart.


###### Response

The response to this webhook is expected to contain:

* `cart_items` - Array of Objects.
    * `cart_id` - Integer. Must match the `cart_id` sent in the request
    * `description` - String. Optional Item level discount description.
    * `discount_amount` - Decimal. The discount that should be applied for this item.
* `add_items` - Array of Objects. New items that will be added to the cart as part of the discount.
    * `price` - Decimal.
    * `product_id` - Integer. ID of the [`product`](resources/products.md)
    * `quantity` - Integer.
    * `variant_inventory_item_number` - [`variant inventory`](resources/variant_inventory.md) item number
    * `variants` - Array of Objects. If using variant inventory set `variant_inventory_item_number` instead of this array.
        * `group` - String. Variant group name
        * `value` - String. Variant name
* `description` - Array of String. Optional description of all discounts applied.
* `discount` - Decimal. Discount amount will be used in addition to any `cart_items.discount_amount`
* `shipping_discount` - Decimal. Specify this amount if shipping should be discounted separately.

