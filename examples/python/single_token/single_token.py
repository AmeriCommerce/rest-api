# The 'requests' module is available via pip: "pip install requests"
# You can find more documentation about requests at http://docs.python-requests.org/en/latest/
import requests
import json
import locale
import sys

STORE_DOMAIN = "<< YOUR STORE DOMAIN >>"
ACCESS_TOKEN = "<< YOUR ACCESS TOKEN >>"

locale.setlocale(locale.LC_ALL, '')

def get_product_list(token):
    headers = {
        'X-AC-Auth-Token': ACCESS_TOKEN
    }
    uri = 'https://{}/api/v1/products'.format(STORE_DOMAIN)
    # include verify=False if using dev certificate
    # r = requests.get(uri, headers = headers, verify = False)
    r = requests.get(uri, headers = headers)
    return r.json()


if __name__ == '__main__':
    product_list = get_product_list(ACCESS_TOKEN)

    for product in product_list['products']:
        encoded_name = product['item_name'].encode('utf-8')
        line_end = ": {}\n".format(locale.currency(product['price']), grouping = True).encode('utf-8')
        sys.stdout.buffer.write(encoded_name + line_end)