products
========

```shell
GET /api/v1/products
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 18,
	"item_number": "",
	"supplier_id": 0,
	"manufacturer_id": 0,
	"manufacturer_part_number": "",
	"primary_category_id": 11,
	"product_status_id": 1,
	"item_name": "Natalie Dining Table Set",
	"bullets": "",
	"short_description": "",
	"long_description_2": "<ul>\r\n<li>\r\n<div class=\"\"><font face=Verdana size=1>Material: Chromed metal, clear glass</font></div>\r\n<li>\r\n<div class=\"\"><font face=Verdana size=1>Dimension (L x W x H): 55\" - 80\"W x 32\"D x 30\"H (140-200cm x 90cm x 74cm)</font></div>\r\n<li>\r\n<div class=\"\"><font face=Verdana size=1>Glass thickness: 0.4” (10mm)</font></div>\r\n<li>\r\n<div class=\"\"><font face=Verdana size=1>Weight: 72 kg / 159 lbs</font></div>\r\n<li>\r\n<div class=\"\"><font face=Verdana size=1>Care: household glass cleaner only on glass </font></div></li></ul>",
	"long_description_3": "",
	"long_description_4": "",
	"long_description_5": "",
	"height": "",
	"length": "",
	"width": "",
	"size_unit": "In",
	"weight": 1,
	"weight_unit": "Lbs",
	"cost": 0,
	"price": 589,
	"retail": 689,
	"minimum_quantity": 0,
	"maximum_quantity": 0,
	"is_spotlight_item": 1,
	"quantity_on_hand": 0,
	"keywords": "",
	"is_non_taxable": 0,
	"is_shipped_individually": 0,
	"is_hidden": 0,
	"sort_order": 0,
	"e_product_type": "NotAnEProduct",
	"e_product_url": "",
	"e_product_password": "",
	"e_product_verification_link_expiration": 0,
	"e_product_email": "",
	"e_product_allow_multiple_deliveries": 0,
	"warehouse_id": 0,
	"call_for_shipping": 0,
	"call_for_pricing": 0,
	"rate_adjustment_type": "AutoCalculation",
	"meta_description": "",
	"page_title": "",
	"use_tabs": false,
	"related_name": "",
	"override_theme_use_tabs": false,
	"long_description_tab_name_1": "",
	"long_description_tab_name_2": "",
	"long_description_tab_name_3": "",
	"long_description_tab_name_4": "",
	"long_description_tab_name_5": "",
	"long_description_1": "Always ready to impress your guests, this table combines style and functionality with the clear tempered glass on top of the chrome-finished metal frame. The built in simple mechanism will extend the table. The simple mechanism will work for you to extract the hidden extension from the middle when you pull the glass table top. Add a contemporary touch to your dining room today. ",
	"is_non_shipping_item": false,
	"e_product_delivery_action": "None",
	"use_variant_inventory": false,
	"is_featured_item": false,
	"long_description_external_url_1": "",
	"long_description_external_url_2": "",
	"long_description_external_url_3": "",
	"long_description_external_url_4": "",
	"long_description_external_url_5": "",
	"bullets_external_url": "",
	"custom_flag_1": false,
	"custom_flag_2": false,
	"custom_flag_3": false,
	"custom_flag_4": false,
	"custom_flag_5": false,
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"url_rewrite": "",
	"is_kit": false,
	"is_child_product": false,
	"is_non_inventory": false,
	"is_discontinued": false,
	"eta_date": null,
	"quantity_on_order": 0,
	"available_region_id": null,
	"call_for_shipping_on_whole_order": false,
	"break_out_shipping": false,
	"shipping_classification_code": "",
	"exclude_parent_from_display": false,
	"drop_ship": false,
	"no_price_mask": "",
	"starting_quantity": null,
	"tax_code": "",
	"use_map_pricing": false,
	"last_item_number": "",
	"has_visible_variants": false,
	"product_rating_dimension_group_override_id": null,
	"average_review_rating": null,
	"review_count": null,
	"exclude_children_from_display": false,
	"use_pricing_from_parent": false,
	"low_stock_warning_threshold": null,
	"enable_low_stock_warning": false,
	"do_not_discount": false,
	"head_tags": "",
	"handling_fee": null,
	"custom_upsell_url": "",
	"e_product_serial_number_file_path": "",
	"hide_variant_surcharges": false,
	"quantity_increment": 1,
	"gtin": "",
	"add_to_cart_message": "",
	"is_subscription_product": false,
	"subscription_frequency": null,
	"subscription_frequency_type": "",
	"e_product_generic_username": "",
	"e_product_generic_password": "",
	"shipping_override": null,
	"insurance_cost": null,
	"exclude_from_commissions": false,
	"days_until_reorder_allowed": 0,
	"force_separate_order": false,
	"approval_required": false,
	"in_stock_notification_email_template_id": null,
	"inelligible_for_purchase_by_points": false,
	"earns_points": true,
	"additional_points_earned": null,
	"allowed_variable_subscription_types": "",
	"profile_id": null
}
```

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/products/{id}/{nested_resource}`.

### variants

```shell
GET /api/v1/products?expand=variants
```

```shell
GET /api/v1/products/{id}/variants
```

```json
{
	...
	"variants": [
		{
			"id": 11,
			"variant_group_id": 7,
			"description": "Director's Cut",
			"price_adjustment": 2,
			"price_adjustment_type": "+ dollars",
			"sort_order": 0,
			"item_number_extension": "",
			"is_hidden": false,
			"updated_at": null,
			"created_at": null,
			"is_default_selection": false
		},
		...
	],
	...
}
```

### personalizations

```shell
GET /api/v1/products?expand=personalizations
```

```shell
GET /api/v1/products/{id}/personalizations
```

```json
{
	...
	"personalizations": [
		{
			"id": 3,
			"question": "Wat is your favorite color?",
			"is_required": false,
			"sort_order": 0,
			"is_multi_line": false,
			"updated_at": "2014-03-07T13:44:13.187-06:00",
			"created_at": "2014-03-07T13:44:13.187-06:00",
			"display_type": "TextBox",
			"max_length": null,
			"markup_fee": 0,
			"is_step": false,
			"step_group": 0
		},
		...
	],
	...
}
```

### related

```shell
GET /api/v1/products?expand=related
```

```shell
GET /api/v1/products/{id}/related
```

```json
{
	...
	"related": [
		{
			"id": 6,
			"sort_order": 0,
			"is_hidden": false,
			"is_upsell": false
		},
		{
			"id": 7,
			"sort_order": 0,
			"is_hidden": false,
			"is_upsell": false
		},
		...
	],
	...
}
```

### categories

```shell
GET /api/v1/products?expand=categories
```

```shell
GET /api/v1/products/{id}/categories
```

```json
{
	...
	"categories": [
		{
			"id": 1,
			"is_primary": false,
			"name": "DVD Movies"
		},
		{
			"id": 8,
			"is_primary": false,
			"name": "Action"
		},
		{
			"id": 3,
			"is_primary": true,
			"name": "Electronics"
		},
		...
	],
	...
}
```

### pricing

```shell
GET /api/v1/products?expand=pricing
```

```shell
GET /api/v1/products/{id}/pricing
```

```json
{
	...
	"pricing": [
		{
			"id": 31,
			"store_id": null,
			"customer_type_id": null,
			"variant_inventory_id": null,
			"sale_type_id": null,
			"start_date": null,
			"end_date": null,
			"starting_quantity": 1,
			"price": 160,
			"cost": 50,
			"updated_at": null,
			"created_at": null,
			"price_calculation_id": null,
			"variant_id": null,
			"variant_price_surcharge": ""
		},
		{
			"id": 32,
			"store_id": null,
			"customer_type_id": null,
			"variant_inventory_id": null,
			"sale_type_id": null,
			"start_date": null,
			"end_date": null,
			"starting_quantity": 24,
			"price": 144,
			"cost": 45,
			"updated_at": null,
			"created_at": null,
			"price_calculation_id": null,
			"variant_id": null,
			"variant_price_surcharge": ""
		},
		...
	],
	...
}
```

### attributes

```shell
GET /api/v1/products?expand=attributes
```

```shell
GET /api/v1/products/{id}/attributes
```

```json
{
	...
	"attributes": [
		{
			"id": 4,
			"attribute_group_id": 1,
			"name": "Air Max",
			"is_hidden": false,
			"sort_order": 0,
			"updated_at": null,
			"created_at": null,
			"page_title": "",
			"keywords": "",
			"meta_description": "",
			"url_rewrite": "",
			"value": ""
		},
		{
			"id": 5,
			"attribute_group_id": 1,
			"name": "Running Shoes",
			"is_hidden": false,
			"sort_order": 0,
			"updated_at": null,
			"created_at": null,
			"page_title": "",
			"keywords": "",
			"meta_description": "",
			"url_rewrite": "",
			"value": ""
		},
		...
	],
	...
}
```

### variant_inventory

```shell
GET /api/v1/products?expand=variant_inventory
```

```shell
GET /api/v1/products/{id}/variant_inventory
```

```json
{
	...
	"variant_inventory": [
		{
			"id": 4,
			"inventory": 5,
			"item_number": "3367799-1",
			"manufacturer_item_number": "",
			"weight": 0,
			"product_status_id": 1,
			"updated_at": null,
			"created_at": null,
			"low_stock_warning_at": null,
			"low_stock_warning_enabled": false,
			"gtin": ""
		},
		...
	],
	...
}
```

### pictures

```shell
GET /api/v1/products?expand=pictures
```

```shell
GET /api/v1/products/{id}/pictures
```

```json
{
	...
	"pictures": [
		{
			"id": 30,
			"image_file": "/images/LG/60_50PY2DR_bic.jpg",
			"alt": "",
			"description": "",
			"is_primary": true,
			"is_hidden": false,
			"thumbnail_file": "/images/LG/_thumb_60_50PY2DR_bic.jpg",
			"sort_order": 0,
			"flash_path": "",
			"created_at": "2013-10-17T20:09:47.327-05:00",
			"updated_at": "2013-10-17T20:09:47.327-05:00",
			"is_video_screen_shot": false,
			"video_content": ""
		},
		...
	],
	...
}
```

### shipping_rate_adjustments

```shell
GET /api/v1/products?expand=shipping_rate_adjustments
```

```shell
GET /api/v1/products/{id}/shipping_rate_adjustments
```

```json
{
	...
	"shipping_rate_adjustments": [
		{
			"id": 3754,
			"type": "Flat Rate",
			"amount": 0,
			"shipping_method_name": "UPS Ground",
			"shipping_provider": "UPS",
			"is_unavailable": false,
			"updated_at": null,
			"created_at": null,
			"available_region_id": null
		},
		{
			"id": 3755,
			"type": "Flat Rate",
			"amount": 0,
			"shipping_method_name": "UPS Next Day Air",
			"shipping_provider": "UPS",
			"is_unavailable": false,
			"updated_at": null,
			"created_at": null,
			"available_region_id": null
		},
		...
	],
	...
}
```

### reviews

```shell
GET /api/v1/products?expand=reviews
```

```shell
GET /api/v1/products/{id}/reviews
```

```json
{
	...
	"reviews": [
		{
			"id": 1,
			"title": "Lorem ipsum Cillum amet minim ex eiusmod.",
			"body": "Lorem ipsum Dolore qui consectetur incididunt deserunt qui id sit Excepteur sit dolor anim ex quis reprehenderit.",
			"review_pros": "",
			"review_cons": "",
			"overall_rating": 5,
			"customer_id": null,
			"approved_by_user_id": null,
			"approved_at": null,
			"created_at": "2014-04-16T13:35:20.6-05:00",
			"updated_at": "2014-04-16T13:35:20.6-05:00",
			"author_display_name": "some guy",
			"author_email": "test@nope.xyz",
			"author_website": "",
			"author_location": "",
			"approval_status": "Approved",
			"origin_store_id": 3
		},
		...
	],
	...
}
```

### child_products

```shell
GET /api/v1/products?expand=child_products
```

```shell
GET /api/v1/products/{id}/child_products
```

```json
{
	...
	"child_products": [
		{
			"id": 24,
			"item_number": "",
			"supplier_id": 0,
			"manufacturer_id": 0,
			"manufacturer_part_number": "",
			"primary_category_id": 7,
			"product_status_id": 1,
			"item_name": "Veggie Tales - Minnesota Cuke",
			"bullets": "",
			"short_description": "Hold on to your hats, adventure lovers! It's the most mysterious and intriguing VeggieTales ever!",
			"long_description_2": "",
			"long_description_3": "",
			"long_description_4": "",
			"long_description_5": "",
			"height": "",
			"length": "",
			"width": "",
			"size_unit": "1",
			"weight": 1,
			"weight_unit": "1",
			"cost": 0,
			"price": 9.95,
			"retail": 19.95,
			"minimum_quantity": 0,
			"maximum_quantity": 0,
			"is_spotlight_item": 0,
			"quantity_on_hand": 100,
			"keywords": "",
			"is_non_taxable": 0,
			"is_shipped_individually": 0,
			"is_hidden": 0,
			"sort_order": 0,
			"e_product_type": "0",
			"e_product_url": "",
			"e_product_password": "",
			"e_product_verification_link_expiration": 0,
			"e_product_email": "",
			"e_product_allow_multiple_deliveries": 1,
			"warehouse_id": 0,
			"call_for_shipping": 0,
			"call_for_pricing": 0,
			"rate_adjustment_type": "0",
			"meta_description": "",
			"page_title": "",
			"use_tabs": true,
			"related_name": "",
			"override_theme_use_tabs": false,
			"long_description_tab_name_1": "",
			"long_description_tab_name_2": "",
			"long_description_tab_name_3": "",
			"long_description_tab_name_4": "",
			"long_description_tab_name_5": "",
			"long_description_1": "<P>Larry the Cucumber stars at Minnesota Cuke -- peaceful children's museum curator by trade, daring explorer in a fedora at heart! When Cuke learns of the legendary hairbrush of Samson, he ponders using its powers to defeat his life-long nemesis, Professor Rattan. Rattan has bullied Cuke since the second grade, leaving him tempted to retaliate. \r\n<P>Will Minnesota hold the hairbrush for selfish gain, or will he find the power to forgive his enemy? Grab your passports and join Cuke, Martin (Bob the Tomato), Rattan and the VeggieTales gang on their adventurous journey in the search for Samson's hairbrush -- and a better way to deal with bullies! \r\n<P>Also find out what's going on with Junior Asparagus as he faces a bully on the playground!</P>",
			"is_non_shipping_item": false,
			"e_product_delivery_action": null,
			"use_variant_inventory": false,
			"is_featured_item": false,
			"long_description_external_url_1": "",
			"long_description_external_url_2": "",
			"long_description_external_url_3": "",
			"long_description_external_url_4": "",
			"long_description_external_url_5": "",
			"bullets_external_url": "",
			"custom_flag_1": false,
			"custom_flag_2": false,
			"custom_flag_3": false,
			"custom_flag_4": false,
			"custom_flag_5": false,
			"created_at": null,
			"updated_at": "2014-06-09T15:12:26.483-05:00",
			"url_rewrite": "",
			"is_kit": true,
			"is_child_product": true,
			"is_non_inventory": false,
			"is_discontinued": false,
			"eta_date": null,
			"quantity_on_order": 0,
			"available_region_id": null,
			"call_for_shipping_on_whole_order": false,
			"break_out_shipping": false,
			"shipping_classification_code": "",
			"exclude_parent_from_display": false,
			"drop_ship": false,
			"no_price_mask": "",
			"starting_quantity": null,
			"tax_code": "",
			"use_map_pricing": false,
			"last_item_number": "",
			"has_visible_variants": false,
			"product_rating_dimension_group_override_id": null,
			"average_review_rating": 0,
			"review_count": 0,
			"exclude_children_from_display": false,
			"use_pricing_from_parent": false,
			"low_stock_warning_threshold": null,
			"enable_low_stock_warning": false,
			"do_not_discount": false,
			"head_tags": "",
			"handling_fee": null,
			"custom_upsell_url": "",
			"e_product_serial_number_file_path": "",
			"hide_variant_surcharges": false,
			"quantity_increment": 1,
			"gtin": "",
			"add_to_cart_message": "",
			"is_subscription_product": false,
			"subscription_frequency": null,
			"subscription_frequency_type": "",
			"e_product_generic_username": "",
			"e_product_generic_password": "",
			"shipping_override": null,
			"insurance_cost": null,
			"exclude_from_commissions": false,
			"days_until_reorder_allowed": 0,
			"force_separate_order": false,
			"approval_required": false,
			"in_stock_notification_email_template_id": null,
			"inelligible_for_purchase_by_points": false,
			"earns_points": true,
			"additional_points_earned": null,
			"allowed_variable_subscription_types": "",
			"profile_id": null,
			"is_default_child": false,
			"bind_quantity_to_parent": false,
			"is_required": false
		},
		...
	],
	...
}
```

### custom_fields

```shell
GET /api/v1/products?expand=custom_fields
```

```shell
GET /api/v1/products/{id}/custom_fields
```

```json
{
	...
	"custom_fields": [
		{
			"name": "testme",
			"value": "my value"
		},
		...
	],
	...
}
```