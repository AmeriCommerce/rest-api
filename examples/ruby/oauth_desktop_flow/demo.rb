require './americommerce_api'

api = AmeriCommerce::ApiClient.new

token = api.get_token('<< USER NAME >>', '<< USER API KEY >>')

product_list = api.get_product_list(token)

product_list['products'].each do |product|
	puts "#{product['item_name']}: #{product['price']}"
end