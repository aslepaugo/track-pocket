from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        'id': 1,
        'name': 'Jabłko',
        'price': 2.58

    },
    {
        'id': 2,
        'name': 'Bułka Paryska',
        'price': 1.69

    },
    {
        'id': 3,
        'name': 'Mleko Polskie',
        'price': 2.59

    },
    
]

def valid_product(product_object):
    if "name" in product_object and "id" in product_object and "price" in product_object:
        return True
    else:
        return False


@app.route("/products")
def get_products():
    return jsonify({'products': products})


@app.route("/products", methods=['POST'])
def add_book():
    request_data = request.get_data()
    if valid_product(request_data):
        products.insert(0, request_data)
        return "True"
    else:
        return "False"



@app.route("/products/<int:id>")
def get_product_by_id(id):
    return_value = {}
    for product in products:
        if product['id'] == id :
            return_value = {
                'id': product['id'],
                'name': product['name'],
                'price': product['price']
            }
    return jsonify(return_value)


app.run(port=5000)