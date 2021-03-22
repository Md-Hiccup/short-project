from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
    # return '<h1>Hello, World!</h1>'

## Dynamic Route
# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is the about page of {username}</h1>'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        { 'id': 1, 'name': 'Phone', 'barcode': '8933224455697', 'price': 500},
        { 'id': 2, 'name': 'Laptop', 'barcode': '4554323322756', 'price': 900},
        { 'id': 3, 'name': 'Keboard', 'barcode': '3242564455601', 'price': 150}
    ]
    return render_template('market.html', items=items)