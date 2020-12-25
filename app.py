from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import os

from BusinessObject import Customer as CustomerEntity
from DataObject import Customer

app = Flask(__name__)
CORS(app)

connection_data = dict()
connection_data['host'] = os.getenv('host')
connection_data['user'] = os.getenv('user')
connection_data['password'] = os.getenv('password')
connection_data['port'] = os.getenv('port')
connection_data['database'] = os.getenv('database')

@app.route('/')
def home():
    return 'This is backend'

@app.route('/index', methods=['GET'])
def index():
    return 'This is index page'

# CRUD(Create, Read, Update, Delete)
# POST, GET, PUT, DELETE

@app.route('/customer', methods=['POST'])
def add_customer():
    data = request.json
    customer = CustomerEntity(customer_name=data['customer_name'],
                                contact_name=data['contact_name'],
                                address=data['address'],
                                city=data['city'],
                                postal_code=data['postal_code'],
                                country=data['country'])
    c = Customer(connection_data)
    message = c.insert(customer)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/customer/all')
def get_all_customer():
    c = Customer(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/customer/<int:id>', methods=['DELETE', 'PUT'])
def delete_customer_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        customer = CustomerEntity(customer_id=id)
        c = Customer(connection_data)
        result = c.delete(customer)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        customer = CustomerEntity(customer_id=id,
                                    customer_name=data['customer_name'],
                                    contact_name=data['contact_name'],
                                    address=data['address'],
                                    city=data['city'],
                                    postal_code=data['postal_code'],
                                    country=data['country'])
        c = Customer(connection_data)
        result = c.update(customer)
        return jsonify({
            'message': result[0]
        }), result[1]