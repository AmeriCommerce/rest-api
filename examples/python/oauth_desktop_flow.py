# The 'requests' module is available via pip: "pip install requests"
# You can find more documentation about requests at http://docs.python-requests.org/en/latest/
import requests
import json
import sys
import locale
from hashlib import sha256

APP_ID = 1
APP_SECRET = "YOUR_SECRET_DO_NOT_EXPOSE_THIS"
APP_DOMAIN = 'https://[your store domain]/api'
APP_SCOPE = 'catalog'


class AmeriCommerceApi():

    def __init__(self, username, key):
        self.username = username
        self.key = key
        self.get_access_token()

    def get_access_token(self):
        response = self.oauth_init()
        response = self.request_token(**response)
        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']
        self.expires = response['expires']

    def create_sig(self, *args):
        combined = "".join([str(s) for s in args]).encode(encoding = 'UTF-8')
        return sha256(combined).hexdigest()

    def oauth_init(self):
        sig = self.create_sig(APP_SECRET, self.username, self.key, APP_ID, APP_SCOPE, APP_DOMAIN)
        headers = {
            'content-type': 'application/json'
        }
        body = {
            'app_id': APP_ID,
            'scope': APP_SCOPE,
            'redirect_url': APP_DOMAIN,
            'username': self.username,
            'signature': sig
        }
        r = requests.post(APP_DOMAIN + '/oauth', headers = headers, data = json.dumps(body))
        return r.json()

    def request_token(self, ref, code):
        sig = self.create_sig(APP_SECRET, code, APP_ID, APP_SCOPE, APP_DOMAIN)
        headers = {
            'content-type': 'application/json'
        }
        body = {
            'app_id': APP_ID,
            'ref': ref,
            'signature': sig
        }
        r = requests.post(APP_DOMAIN + '/oauth/access_token', headers = headers, data = json.dumps(body))
        return r.json()

    def get_product_list(self):
        headers = {
            'content-type': 'application/json',
            'x-ac-auth-token': self.access_token
        }
        r = requests.get(APP_DOMAIN + '/v1/products', headers = headers)
        return r.json()


if __name__ == '__main__':
    username = input("Username: ")
    key = input("API Key: ")
    api = AmeriCommerceApi(username, key)
    locale.setlocale(locale.LC_ALL, '')

    product_result = api.get_product_list()
    for product in product_result['products']:
        # This encoding thing shouldn't be necessary on non-Windows platforms, but the Windows console has pretty big
        # character printing limitations so it's easier to just print out the utf-8 byte string
        encoded_name = product['item_name'].encode('utf-8')
        print(encoded_name, locale.currency(product['price'], grouping = True))