from flask import Flask
from models import db
from schemas import ma
from config import Config

# Import route blueprints
from routes.user_routes import users_bp
from routes.product_routes import products_bp
from routes.order_routes import orders_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
ma.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)
app.register_blueprint(orders_bp)

if __name__ == '__main__':
    app.run(debug=True)