# The 'requests' module is available via pip: "pip install requests"
# You can find more documentation about requests at http://docs.python-requests.org/en/latest/
import requests
import json
import locale
import sys

STORE_DOMAIN = "<< YOUR STORE DOMAIN >>"
ACCESS_TOKEN = "<< YOUR ACCESS TOKEN >>"
STORE_ID = 1  # This should reflect your store's ID

locale.setlocale(locale.LC_ALL, '')

# Searches for and returns the customer that matches the info passed in,
# if no customer is found a new one is created and returned
def get_customer(firstName, lastName, email):
	
	# setup headers
	headers = {
		'X-AC-Auth-Token': ACCESS_TOKEN,
		'Content-Type': 'application/json'
    }
	
	# build API call to check if customer already exists (using email)
	uri = 'https://{}/api/v1/customers?email={}'.format(STORE_DOMAIN, email)
    
	# include verify=False if using dev certificate
	# r = requests.get(uri, headers = headers, verify=False)
	r = requests.get(uri, headers = headers)
	
	# see if a customer was found
	customer = r.json()
	if (customer['total_count'] > 0):
		return customer['customers'][0];
		
	# no customer found, so lets create a new one
	data = {
		'last_name': lastName,
		'first_name': firstName,
		'email': email,
		'store_id': STORE_ID
	}
	
	# build API call to post a new customer
	uri = 'https://{}/api/v1/customers'.format(STORE_DOMAIN)
	
	# include verify=False if using dev certificate
	# r = requests.post(uri, headers=headers, data = json.dumps(data), verify=False)
	r = requests.post(uri, headers=headers, data = json.dumps(data))
	
	# return newly created customer
	return r.json()
	
if __name__ == '__main__':
	customer = get_customer('John', 'Doe', 'JohnDoe@email.com')
	first_name = customer['first_name'].encode('utf-8')
	last_name = ',{}\n'.format(customer['last_name']).encode('utf-8')
	email = customer['email'].encode('utf-8')
	sys.stdout.buffer.write(first_name + last_name + email)
