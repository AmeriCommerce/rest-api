# The 'requests' module is available via pip: "pip install requests"
# You can find more documentation about requests at http://docs.python-requests.org/en/latest/
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

    def get_token(self, username, api_key):
        temp = self._start_negotiation(username, api_key)
        token_data = self._verify(**temp)
        return Token(token_data)

    def get_product_list(self, token):
        headers = {
            'x-ac-auth-token': token.access_token
        }
        uri = "https://{}/api/v1/products".format(self.store_domain)
        r = requests.get(uri, headers = headers)
        return r.json()

    def _start_negotiation(self, username, api_key):
        sig = self._create_signature(self.app_secret, username, api_key, self.app_id, self.app_scope, self.store_domain)
        headers = {
            'content-type': 'application/json'
        }
        body = {
            'app_id': self.app_id,
            'scope': self.app_scope,
            'redirect_url': self.store_domain,
            'username': username,
            'signature': sig
        }
        uri = "https://{}/api/oauth".format(self.store_domain)
        r = requests.post(uri, headers = headers, data = json.dumps(body))
        return r.json()

    def _verify(self, auth_id, code):
        sig = self._create_signature(self.app_secret, code, self.app_id, self.app_scope, self.store_domain)
        headers = {
            'content-type': 'application/json'
        }
        body = {
            'app_id': self.app_id,
            'auth_id': auth_id,
            'signature': sig
        }
        uri = "https://{}/api/oauth/access_token".format(self.store_domain)
        r = requests.post(uri, headers = headers, data = json.dumps(body))
        return r.json()

    def _create_signature(self, *args):
        combined = "".join([str(s) for s in args]).encode(encoding = 'UTF-8')
        return sha256(combined).hexdigest()


class Token():

    def __init__(self, data):
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
        self.expires = data['expires']