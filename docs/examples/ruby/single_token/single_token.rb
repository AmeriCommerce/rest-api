require 'json'
require 'net/http'
require 'uri'
require 'openssl'

STORE_DOMAIN = '<< YOUR STORE DOMAIN >>'
ACCESS_TOKEN = '<< YOUR ACCESS TOKEN >>'

def get_product_list(token)
	headers = {
		'X-AC-Auth-Token' => ACCESS_TOKEN
	}
	uri = URI("https://#{STORE_DOMAIN}/api/v1/products")
	http = Net::HTTP.new(uri.host, uri.port)
	http.use_ssl = true
	# if using a development cert
	# http.verify_mode = OpenSSL::SSL::VERIFY_NONE

	response = http.get(uri.path, headers)
	JSON.parse(response.body)
end

product_list = get_product_list(ACCESS_TOKEN)

product_list['products'].each do |product|
	puts "#{product['item_name']}: #{product['price']}"
end