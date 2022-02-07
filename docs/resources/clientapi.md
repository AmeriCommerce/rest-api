# AmeriCommerce Client API Samples 



[Please click here to navigate to the github repo](https://github.com/AmeriCommerce/js-api-samples). Individual examples are separated into directories under src. These examples make use of jQuery.

## Examples 
---

### [Adding to Cart](https://github.com/AmeriCommerce/js-api-samples/tree/master/src/adding_to_cart)

This example explores a basic use case of adding an item to the cart, displaying the new count of items in the cart, and clearing the cart.

### [Updating](https://github.com/AmeriCommerce/js-api-samples/tree/master/src/updating) 

A more advanced example where we lay out a full cart display and attach events to update quantities and remove items from the cart.

### [Embed Tools](https://github.com/AmeriCommerce/js-api-samples/tree/master/src/embed_tools)

Code snippets pulled from the 2012.6 Embed Tools feature.

### [Searching](https://github.com/AmeriCommerce/js-api-samples/tree/master/src/searching)

## Notes 

### Conventions 

Generally a variable that represents a jQuery object will be prefixed with a $. This is purely a convenience that allows us to identify these objects at a glance.

### Version 2012.6 Compatibility 

2012.6 changes the "response.cart" property to "response.data" and standardizes on "response.data" in responses that are not cart-related in nature. As such, you will see the following assignment until 2012.6 has been deployed and is in more widespread use:

    var cart = response.cart || response.data;

That is, it will use cart if it is available, otherwise it will use data. This is safe to use in any version before 2012.6 as well as after.