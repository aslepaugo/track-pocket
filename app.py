from flask import Flask, jsonify, request, Response
import json

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
    if ("name" in product_object and "id" in product_object and "price" in product_object):
        return True
    else:
        return False


@app.route("/products")
def get_products():
    return jsonify({'products': products})


@app.route("/products", methods=['POST'])
def add_book():
    request_data = request.get_json()

    if valid_product(request_data):
        new_product = {
        "id": request_data["id"],
        "name": request_data["name"],
        "price": request_data["price"]
    }
        products.insert(0, new_product)
        response = Response("", 201, mimetype='application/json')
        response.headers["Location"] = "/products/" + str(new_product["id"])
        return response
    else:
        invalid_product_message = {
            "error": "Invalid product passed in request",
            "help": "Please refer to the following link https://help.me/docs/api#post"
        }
        response = Response(json.dumps(invalid_product_message), status = 400, mimetype='application/json')
        return response

@app.route("/products/<int:id>", methods=['PUT'])
def replace_product(id):
    request_data = request.get_json()
    print(request_data)
    new_product = {
        'name': request_data['name'],
        'price': request_data['price'],
        'id': id 
    }

    i = 0
    for product in products:
        currentId = product['id']
        if currentId == id:
            products[i] = new_product
        i += 1
    return Response("", 204)



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