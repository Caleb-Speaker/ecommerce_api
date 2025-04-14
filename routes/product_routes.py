from flask import Blueprint, request, jsonify
from models import db, Product
from schemas import product_schema, products_schema

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify(products_schema.dump(products)), 200

@products_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product_schema.dump(product)), 200

@products_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'product_name' not in data or 'price' not in data:
        return jsonify({"error": "Missing product_name or price"}), 400

    new_product = Product(product_name=data['product_name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()

    return jsonify(product_schema.dump(new_product)), 201

@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()

    if 'product_name' in data:
        product.product_name = data['product_name']
    if 'price' in data:
        product.price = data['price']

    db.session.commit()
    return jsonify(product_schema.dump(product)), 200

@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204