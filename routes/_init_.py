from .user_routes import register_user_routes
from .product_routes import register_product_routes
from .order_routes import register_order_routes

def register_routes(app):
    register_user_routes(app)
    register_product_routes(app)
    register_order_routes(app)