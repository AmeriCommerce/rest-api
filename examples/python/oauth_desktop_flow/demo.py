import americommerce
import sys
import locale

locale.setlocale(locale.LC_ALL, '')

api = americommerce.ApiClient()

token = api.get_token("<< USER NAME >>", "<< USER API KEY >>")

product_list = api.get_product_list(token)

for product in product_list['products']:
    encoded_name = product['item_name'].encode('utf-8')
    line_end = ": {}\n".format(locale.currency(product['price']), grouping = True).encode('utf-8')
    sys.stdout.buffer.write(encoded_name + line_end)