import requests
import json
import sys
from hashlib import sha256

class ApiClient():

    def __init__(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
        self.app_id = config['app_id']
        self.app_secret = config['app_secret']
        self.app_scope = config['app_scope']
        self.store_domain = config['store_domain']

    def start_negotiation(self, return_url):
        return "https://{}/api/oauth?app_id={}&scope={}&redirect_url={}".format(
            self.store_domain, self.app_id, self.app_scope, return_url)

    def verify(self, return_url, auth_id, code):
        sig = self._create_signature(self.app_secret, code, self.app_id, self.app_scope, return_url.lower())
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            'app_id': self.app_id,
            'auth_id': auth_id,
            'signature': sig
        }
        uri = "https://{}/api/oauth/access_token".format(self.store_domain)
        # include verify=False if using dev certificate
        # r = requests.post(uri, headers=headers, data=json.dumps(body), verify=False)
        r = requests.post(uri, headers=headers, data=json.dumps(body))
        return r.json()

    def get_product_list(self, token, page = 1):
        headers = {
            'X-AC-Auth-Token': token
        }
        uri = "https://{}/api/v1/products?page={}".format(self.store_domain, page)
        # include verify=False if using dev certificate
        # r = requests.get(uri, headers=headers, verify=False)
        r = requests.get(uri, headers=headers)
        return r.json()

    def _create_signature(self, *args):
        combined = "".join([str(s) for s in args]).encode(encoding='utf-8')
        return sha256(combined).hexdigest()