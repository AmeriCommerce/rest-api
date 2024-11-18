from flask import Flask, session, redirect, url_for, request, render_template
import americommerce
from urllib.parse import urlparse, parse_qs, quote

app = Flask(__name__)
api = americommerce.ApiClient()

def encode_redirect_url(redirect_uri):
    # Parse the URL
    parsed_uri = urlparse(redirect_uri)
    
    # Parse query string into dictionary
    qs = parse_qs(parsed_uri.query, keep_blank_values=True)
    
    # Get the base URL without query parameters
    base_url = f"{parsed_uri.scheme}://{parsed_uri.netloc}{parsed_uri.path}"
    
    # Encode only the values in the query parameters
    if qs:
        # For each parameter value, encode it if it's not already encoded
        encoded_pairs = []
        for key, values in qs.items():
            if values:
                # Encode the value if it contains unencoded characters
                encoded_value = quote(values[0], safe='')
                encoded_pairs.append(f"{key}={encoded_value}")
        
        query_string = "&".join(encoded_pairs)
        return f"{base_url}?{query_string}"
    
    return base_url

@app.route("/")
def index():
    if not 'api_user' in session:
        r = request.base_url
        return_url = url_for('callback', r=r, _external=True)
        encoded_return_url = encode_redirect_url(return_url).lower()
        return redirect(api.start_negotiation(encoded_return_url))

    token = session['api_user']
    page = request.args.get('page', 1, type=int)
    product_list = api.get_product_list(token['access_token'], page)
    next_button_class = 'next'
    previous_button_class = 'previous'

    if not 'next_page' in product_list:
        next_button_class += ' disabled'
    if not 'previous_page' in product_list:
        previous_button_class += ' disabled'

    return render_template('product_list.jinja',
        product_list=product_list,
        next_button_class=next_button_class,
        previous_button_class=previous_button_class,
        current_page=page)

@app.route("/callback")
def callback():
    r = request.args.get('r', '')
    return_url = url_for('callback', r=r, _external=True)
    encoded_return_url = encode_redirect_url(return_url)
    token_data = api.verify(encoded_return_url, request.args.get('auth_id', ''), request.args.get('code', ''))
    print(token_data)
    session['api_user'] = token_data
    return redirect(r)

if __name__ == "__main__":
    # generate your own key for a real app, don't use this one
    app.secret_key = b"\x8d.\x9bS\x98J^\x81\x96h\x15\xe2'\x82\xa4\x87\x90#d\xe9\x8c\xd0k\x06"
    app.run(debug=True)