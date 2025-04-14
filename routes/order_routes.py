from flask import Blueprint, request, jsonify
from models import db, Order, Product, User
from schemas import order_schema, orders_schema
from datetime import datetime

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify(orders_schema.dump(orders)), 200

@orders_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order_schema.dump(order)), 200

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'user_id' not in data or 'product_ids' not in data:
        return jsonify({"error": "Missing user_id or product_ids"}), 400
    
    found_user = User.query.get(data['user_id'])
    if found_user == None:
        return jsonify({"error": "Cannot find user"}), 400

    new_order = Order(user_id=data['user_id'], order_date=datetime.utcnow())

    for pid in data['product_ids']:
        product = Product.query.get(pid)
        if not product:
            return jsonify({"error": f"Product with ID {pid} not found"}), 400
        new_order.products.append(product)

    db.session.add(new_order)
    db.session.commit()
    return jsonify(order_schema.dump(new_order)), 201

@orders_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    # Added messsage about successfully deleting 
    return jsonify({"message": f"Order with ID {id} deleted successfully."}), 200
