# The 'requests' module is available via pip: "pip install requests"
# You can find more documentation about requests at http://docs.python-requests.org/en/latest/
import requests
import json
import locale
import sys
import time
from urllib.parse import urlencode

locale.setlocale(locale.LC_ALL, '')

STORE_DOMAIN = "<< YOUR STORE DOMAIN >>"
ACCESS_TOKEN = "<< YOUR ACCESS TOKEN >>"
STORE_ID = 1  # This should reflect your store's ID
CURRENT_TIME = time.strftime('%Y-%m-%dT%H:%M:%S-06:00')

# setup headers
HEADERS = {
        'X-AC-Auth-Token': ACCESS_TOKEN,
        'Content-Type': 'application/json'
}

# Creates one shipment containing all of the order items for an order
def create_shipment(order, shipping_info):

        # create order_items
        order_items = []
        for item in order['items']:
                order_items.append({
                        'id': item['id'],
                        'quantity_shipped': item['quantity'],
                        'product_id': item['product_id'],
                        'item_name': item['item_name']
                })

        # populate data
        data = {
                'order_id': order['id'],
                'shipped_at': CURRENT_TIME,
                'shipping_method': shipping_info['shipping_method_name'],
                'shipping_method_id': shipping_info['shipping_method_id'],
                'shipping_method_type': shipping_info['shipping_method_type'],
                'number_of_packages': 1,
                'total_weight': sum(row['weight'] for row in order['items']),
                'provider_base_shipping_cost': order['shipping_total'],
                'provider_total_shipping_cost': order['shipping_total'],
                'email_sent': False,
                'items': order_items,
                'shipment_name': 'Shipment 1'
                
                # any other data for the shipment goes here
                # for all fields - https://github.com/AmeriCommerce/rest-api/blob/master/resources/order_shipments.md
        }

        # build API call to post new shipment
        uri = 'https://{}/api/v1/order_shipments'.format(STORE_DOMAIN)

        # include verify=False if using dev certificate
        r = requests.post(uri, headers=HEADERS, data=json.dumps(data), verify=False)

        # return newly created shipment
        return r.json()


# Gets order for id
def get_order(id):

        # build API call to get order with items list expanded
        uri = 'https://{}/api/v1/orders/{}?expand=items'.format(STORE_DOMAIN, id)

        # include verify=False if using dev certificate
        r = requests.get(uri, headers=HEADERS, verify=False)

        #return order
        return r.json()


# Gets shipping method info from order
def get_shipping_method(order):

        shipping_info = {
                'shipping_method_id': '',
                'shipping_method_type': '',
                'shipping_method_name': ''
        }
        
        # build API call to check if shipping method is a provider service
        uri = 'https://{}/api/v1/shipping_provider_services?{}'\
              .format(STORE_DOMAIN, urlencode({'identifier': order['selected_shipping_method']}))

        # include verify=False if using dev certificate
        shipping_method = requests.get(uri, headers=HEADERS, verify=False).json()
        
        # shipping method is a shipping provider, extrapolate the data
        if (shipping_method['total_count'] > 0):
                shipping_info['shipping_method_id'] = shipping_method['services'][0]['id']
                shipping_info['shipping_method_type'] = 'provider'
                shipping_info['shipping_method_name'] = shipping_method['services'][0]['identifier']
        else:
                # not a provider service, build api call to check if shipping method is custom
                uri = 'https://{}/api/v1/custom_shipping_methods?{}'\
                      .format(STORE_DOMAIN, urlencode({'name': order['selected_shipping_method']}))

                # include verify=False if using dev certificate
                shipping_method = requests.get(uri, headers=HEADERS, verify=False).json()

                # shipping method is custom, extraploate the data
                if (shipping_method['total_count'] > 0):
                        shipping_info['shipping_method_id'] = shipping_method['custom_shipping_methods']\
                                                              [0]['id']
                        shipping_info['shipping_method_type'] = 'custom'
                        shipping_info['shipping_method_name'] = shipping_method['custom_shipping_methods']\
                                                                [0]['name']

        return shipping_info
                        
if __name__ == '__main__':
        order_id = 1
        order = get_order(order_id)
        shipping_info =  get_shipping_method(order)
        result = create_shipment(order, shipping_info)
        
        print(result)
