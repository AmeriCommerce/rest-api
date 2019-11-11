from flask import Flask, session, redirect, url_for, request, render_template
import americommerce

app = Flask(__name__)
api = americommerce.ApiClient()

@app.route("/")
def index():
    if not 'api_user' in session:
        r = request.base_url
        return_url = url_for('callback', r=r, _external=True)
        return redirect(api.start_negotiation(return_url))

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
    token_data = api.verify(return_url, request.args.get('auth_id', ''), request.args.get('code', ''))
    print(token_data)
    session['api_user'] = token_data
    return redirect(r)

if __name__ == "__main__":
    # generate your own key for a real app, don't use this one
    app.secret_key = b"\x8d.\x9bS\x98J^\x81\x96h\x15\xe2'\x82\xa4\x87\x90#d\xe9\x8c\xd0k\x06"
    app.run(debug=True)