#!/usr/bin/env python
import json
import urllib2

TOKEN = "YOUR TOKEN"
STORE_API = "https://STORE URL/api/v1/"

def hit_endpoint(uri, token, request_type="GET", data=""):
    headers = {
        'Content-Type': 'application/json',
        'X-AC-Auth-Token': token,
    }

    if request_type == "POST":        
        r = urllib2.Request(uri, data, headers)
    else:
        r = urllib2.Request(uri, headers=headers)

    result = urllib2.urlopen(r)

    return result.read()

def no_product_grouping(simple_product):
    simple_product.exclude_parent_from_display = False
    simple_product.is_kit = False

def parent_info_only(simple_product):
    simple_product.exclude_parent_from_display = True
    simple_product.is_kit = False

def exclude_children(simple_product):
    simple_product.exclude_parent_from_display = True
    simple_product.is_kit = True

def exclude_parent(simple_product):
    simple_product.exclude_parent_from_display = False
    simple_product.is_kit = True

group_types = {"NoProductGrouping": no_product_grouping, 
               "SellItemsIndividuallyParentIsInfoOnly": parent_info_only,
               "ExcludeChildrenFromDisplay": exclude_children, 
               "SellItemsInKitWithParent": exclude_parent}

class SimpleProduct(object):
    "A minimal representation of a product"
    def __init__(this, 
                 id=None,
                 item_number="SimpleItemNumber",
                 price=123.00,
                 cost=61.50,
                 retail=130.00,
                 group_type="NoProductGrouping",
                 item_name="SimpleItem",
                 custom_url= None,
                 is_child_product=False,
                 children = None):

        if id != None:
            this.id = id

        this.item_number = item_number
        this.price = price
        this.cost = cost
        this.item_name = item_name
        this.product_status_id = 1 #In Stock, this id can be queried from /api/v1/product_statuses
        this.primary_category_id = 3 #/api/v1/categories
        this.is_child_product = is_child_product
        this.custom_url = custom_url
        
        if children != None:
            this.child_products = children
            for c in this.child_products:
                c.is_child_product = True

        if (group_type in group_types.keys()):
            group_types[group_type](this)

    def __str__(this):
        "Return a json version of the object"
        result = {}

        for key, value in this.__dict__.iteritems():
            if key == "child_products":
                result[key] = [child.__dict__ for child in this.child_products]
            else:
                result[key] = value

        return json.dumps(result)

    def add(this):
        "POST the product to the store"
        return hit_endpoint(STORE_API + "products", TOKEN, request_type="POST", data=str(this))


def main():
    # Create the child products first
    children = [SimpleProduct(item_number="tgChild1", item_name="tgChildName1"),
                SimpleProduct(item_number="tgChild2", item_name="tgChildName2"),
                SimpleProduct(item_number="tgChild3", item_name="tgChildName3"),
                SimpleProduct(item_number="tgChild4", item_name="tgChildName4")]

    for child in children:
        result = child.add()
        #the item id is required when creating the group
        child.id = json.loads(result)["id"]

    # create a product group
    group_product = SimpleProduct(item_number="TestGroup123", 
                                 group_type="SellItemsInKitWithParent",
                                 item_name="testGroup123_name",
                                 children = children)
    group_product.add()

if __name__ == "__main__":
    main()

