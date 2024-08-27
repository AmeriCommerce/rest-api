categories
==========

```shell
GET /api/v1/categories
```

**Required scope**: `read_catalog`, `catalog`

Sample Model
------------

```json
{
	"id": 1,
	"name": "Shoes",
	"short_description": "",
	"sort_order": 0,
	"is_hidden": false,
	"parent_category_id": 14,
	"max_quantity": 0,
	"category_thumbnail": "",
	"page_title": "",
	"lookup_path": "Clothes > Shoes"
	"keywords": "",
	"meta_description": "",
	"category_image": "",
	"external_content_url": "",
	"is_category_content_displayed": true,
	"are_subcategory_products_displayed": false,
	"url_rewrite": "",
	"updated_at": "2014-03-19T13:31:47.923-05:00",
	"created_at": "2014-03-19T13:31:47.923-05:00",
	"default_product_picture": "",
	"alternate_thumbnail": "",
	"head_tags": "",
	"cat_image_alt_text": "",
	"thumb_image_alt_text": "",
        "is_hide_from_site_maps": false
}
```

Category Tree
-------------

When executing a POST, PUT, or DELETE command against the categories endpoint, you will be modifying the category tree for the site.  When the category tree changes for a site, it must be rebuilt.  The API does not automatically trigger a rebuild because the operation can be expensive, and there is no way to know how many category operations will be performed during a given interaction with the API.  For this reason, we expose the following method:

```shell
POST /api/v1/categories/rebuild_tree
```

This will trigger a background process to rebuild the category tree.  Since this is an asynchronous process, the API call returns immediately with a `204 No Content` response. Category trees can be arbitrarily large, so the operation to rebuild the tree may take some time to complete.

Nested Resources
----------------

Accessible via the `?expand=` parameter or `/api/v1/categories/{id}/{nested_resource}`.

### custom_fields

```shell
GET /api/v1/categories?expand=custom_fields
```

```shell
GET /api/v1/categories/{id}/custom_fields
```

```json
{
	...
	"custom_fields": [
		{
			"name": "CategoryCustomField",
                        "value": ""
		},
		...
	],
	...
}
```

### products

```shell
GET /api/v1/categories?expand=products
```

```shell
GET /api/v1/categories/{id}/products
```

```json
{
	...
	"products": [
		{
			"id": 18,
                        "item_number": "",
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
			"quickbooks_item_id": "123-456"
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
			"earns_points": true,
			"additional_points_earned": null,
			"allowed_variable_subscription_types": "",
			"profile_id": null,
			"is_linked_product": false,
			"master_product_id": 6,
			"do_not_send_review_request": false,
			"pack_slip_sort_order": 3,
			"is_enable_variants_on_parent": false,
			"is_hide_children_on_parent": false,
			"cart_product_id": "00000000-0000-0000-0000-000000000000",
			"enabled_configurator": "None",
			"material_code": "",
			"product_line_code": "",
			"ext_update_date": null,
			"additional_attributes": "",
			"shipper_hq_shipping_groups": "",
			"shipper_hq_dimensional_rule_groups": "",
			"shipper_hq_packing_boxes": "",
			"freight_class": "",
			"hs_code": "",
			"coo": "",
			"hts": "",
			"inelligible_for_purchase_by_points": false,
			"is_exempt_from_min_order_amount": false,
			"category_list": null
		},
		...
	],
	...
}
```
