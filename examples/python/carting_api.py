#!/usr/bin/env python

# The 'requests' module is available via pip: "pip install requests"
# You can find more documentation about requests at http://docs.python-requests.org/en/latest/
import requests
import json
import locale
import sys
import urllib
import time
import datetime
from optparse import OptionParser

STORE_DOMAIN = "<STORENAME.MYSPARKPAY.COM>"
ACCESS_TOKEN = "<TOKEN>"
STORE_ID = 1  # This should reflect your store's ID
TEST_PROD_ID = 5158 #id of a test product

locale.setlocale(locale.LC_ALL, '')


class Address:
    def __init__(this, name, line1, line2, city, state, postal_code, country):
        this.name = name
        this.address_line_1 = line1
        this.address_line_2 = line2
        this.city = city
        this.state = state
        this.postal_code = postal_code
        this.country = country


class Card:
    def __init__(this, number, cvv, expiration_date):
        this.number = number
        this.cvv = cvv
        this.expiration_date = expiration_date


def auth_headers():

    # setup headers
    headers = {
        'X-AC-Auth-Token': ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }

    return headers


def wait_after_call(function):

    def waiter(*args, **kwargs):
        result = function(*args, **kwargs)
        time.sleep(2)
        return result

    return waiter


def build_echo(printer, function):

    def echo(*args, **kwargs):
        result = function(*args, **kwargs)
        printer(result)
        return result

    return echo


def prn(s):
    print s


def prn_json(json_obj):
    print json.dumps(json_obj, indent=4)


def echo_string(function):
    return build_echo(prn, function)


def echo_json(function):
    return build_echo(prn_json, function)

# include verify=False if using dev certificate
def post(uri, data=None):
    return requests.post(uri, headers=auth_headers(), data = json.dumps(data))


def put(uri, data=None):
    return requests.put(uri, headers=auth_headers(), data = json.dumps(data))


def get(uri):
    return requests.get(uri, headers = auth_headers())


@echo_string
def api_url(endpoint, parameter_dictionary=None):

    if parameter_dictionary is None:
        query_string = ""
    else:
        query_string = "?%s" % urllib.urlencode(parameter_dictionary)

    return 'https://{}/api/v1/{}{}'.format(STORE_DOMAIN, endpoint, query_string) 


@wait_after_call
@echo_json
def get_customer(firstName, lastName, email):

    """Searches for and returns the customer that matches the info passed in,
    if no customer is found a new one is created and returned"""

    # build API call to check if customer already exists (using email)
    uri = api_url("customers", {"email": email})
    
    r = get(uri)
    
    # see if a customer was found
    customer = r.json()
    if (customer['total_count'] > 0):
        return customer['customers'][0]
        
    # no customer found, so lets create a new one
    data = {
        'last_name': lastName,
        'first_name': firstName,
        'email': email,
        'store_id': STORE_ID
    }
    
    # build API call to post a new customer
    uri = api_url("customers")
    
    r = post(uri, data)
    
    # return newly created customer
    return r.json()


@wait_after_call
@echo_json
def get_customer_payment_methods(customer_id):
    
    "Returns the customer payment methods currently on file"

    uri = 'https://{}/api/v1/customer_payment_methods?customer_id={}'.format(STORE_DOMAIN, customer_id)
    r = get(uri)

    return r.json()


@wait_after_call
@echo_json
def create_cart():

    "Creates a new empty cart and returns the resource"

    uri = api_url("carts")
    r = post(uri)

    return r.json()


@wait_after_call
@echo_json
def add_item_to_cart(cart, product_id, quantity=1):

    "Add an item to cart using the product_id"

    uri = api_url("carts/%s/items" % cart["id"])

    data = {"items": [
            {"product_id" : product_id,
             "quantity": quantity }]}

    r = post(uri, data)
    return r.json()


@wait_after_call
@echo_json
def calculate_shipping(cart, shipping_address):

    """Calculate shipping, for the items in the cart, to the provided address.
    The items should be added on the server by calling add_item_to_cart"""

    uri = api_url("carts/%s/shipping" % cart["id"], 
            { "city": shipping_address.city,  
              "state": shipping_address.state, 
              "postal_code": shipping_address.postal_code, 
              "country": shipping_address.country})

    r = get(uri)

    return r.json()
    

@wait_after_call
@echo_json
def add_shipping_method(cart, identifier):

    """Adds the shipping to use when placing the order.  The identifier is
    returned from the calculate shipping call."""

    uri = api_url("carts/%s/shipping" % cart["id"])

    data = {"identifier" : identifier}

    r = put(uri, data)

    return r.json()


def get_card_method_id(customer_payment_methods):

    """Pull the default credit card customer payment method.  If that isn't
    found return the first credit card customer payment method.  If a cc method
    isn't found return None"""

    cc_methods = [(cpm["id"], cpm["is_default"])
                  for cpm in customer_payment_methods
                  if cpm["payment_type"] == "CreditCard"]

    default = [id for id, is_default in cc_methods if is_default]

    if len(default) > 0:
        return default[0]
    elif len(cc_methods) > 0:
        return cc_methods[0][0]
    else:
        return None


@wait_after_call
@echo_json
def place_order(cart, customer, address, card):
    """Processes the cart, creating an order"""

    data = { "customer":
            {
                "id": customer["id"],
                "first_name": customer["first_name"],
                "last_name": customer["last_name"],
                "email": customer["email"] },
            "billing_address":
            {
                "name": address.name,
                "address_line_1": address.address_line_1,
                "address_line_2": address.address_line_2,
                "city": address.city,  
                "state": address.state, 
                "postal_code": address.postal_code, 
                "country": address.country},
            "use_billing_address_for_shipping": True}

    if card is None:
        cpmid = get_card_method_id(customer["customer_payment_methods"])

        if cpmid == None:
            raise Exception("Could not find a credit card on file")

        data["credit_card"] = { "cvv": "123"}
        data["customer_payment_method_id"] = cpmid
    else:
        data["credit_card"] = {
                "cvv": "123",
                "number": card.number,
                "name": "%s %s" % (customer["first_name"], customer["last_name"]),
                "expiration_month": card.expiration_date.month,
                "expiration_year": card.expiration_date.year
            }
 
    print "Place order data"
    print json.dumps(data, indent=4)
    uri = api_url("carts/%s/place_order" % cart["id"])

    r = post(uri, data)

    return r.json()


def main(first_name='John', last_name='Doe', email='JohnDoe@email.com', test_card=False):
    customer = get_customer(first_name, last_name, email)

    print " ".join([s.encode('utf-8') for s in 
            [str(customer['id']), 
             customer['first_name'], 
             customer['last_name'], 
             customer['email']]])

    address = Address("%s %s" % (first_name, last_name), "123 Main", "", "Round Rock", "TX", "78681", "US")
    
    cpay = get_customer_payment_methods(customer['id'])
    
    customer["customer_payment_methods"] = cpay["customer_payment_methods"]
    
    cart = create_cart()
    add_item_to_cart(cart, TEST_PROD_ID)
    shipping_rates = calculate_shipping(cart, address)
    rate = add_shipping_method(cart, shipping_rates["rates"][0]["identifier"])

    if test_card:
        cc = Card("4111111111111111", "123", datetime.date(2020, 12, 01))
    else:
        cc = None

    order = place_order(cart, customer, address, cc)
 

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--first_name",
                        action="store",
                        dest="first_name",
                        help="Customer's first name",
                        type="string",
                        default="John")

    parser.add_option("-l", "--last_name",
                        action="store",
                        dest="last_name",
                        help="Customer's last name",
                        type="string",
                        default="Doe")

    parser.add_option("-e", "--email",
                        action="store",
                        dest="email",
                        help="Customer's email",
                        type="string",
                        default="JohnDoe@email.com")

    parser.add_option("-c", "--test_card",
                        action="store_true",
                        dest="test_card",
                        help="Use a test card number?",
                        default=False)
       
    (options, args) = parser.parse_args()

    main(first_name=options.first_name,
         last_name=options.last_name,
         email=options.email,
         test_card=options.test_card)
