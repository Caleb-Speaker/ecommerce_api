Ecommerce API

A simple RESTful API built using Flask for managing users, products, and orders in an ecommerce application. This project uses SQLAlchemy for ORM, Marshmallow for serialization, and includes a modular blueprint structure.

Project Structure

.
├── app.py                  - App entry point
├── config.py               - Configuration settings
├── models.py               - SQLAlchemy models
├── schemas.py              - Marshmallow schemas
├── user_routes.py          - User routes
├── product_routes.py       - Product routes
├── order_routes.py         - Order routes
├── __init__.py             - Route registration (optional)

Getting Started

Prerequisites:
- Python 3.8+
- MySQL Server
- pip for package installation

Installation

1. Clone the repository:
   git clone https://github.com/yourusername/ecommerce-api.git
   cd ecommerce-api

2. Install dependencies:
   pip install flask flask_sqlalchemy flask_marshmallow mysql-connector-python

3. Create the MySQL database:
   CREATE DATABASE ecommerce_api;

4. Update your database credentials in config.py:
   SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:<your-password>@localhost/ecommerce_api'

5. Run the app:
   python app.py

The API will be accessible at http://127.0.0.1:5000/

API Endpoints

Users:
- GET    /users          - List all users
- GET    /users/<id>     - Retrieve a user
- POST   /users          - Create a user
- PUT    /users/<id>     - Update a user
- DELETE /users/<id>     - Delete a user

Products:
- GET    /products       - List all products
- GET    /products/<id>  - Retrieve a product
- POST   /products       - Create a product
- PUT    /products/<id>  - Update a product
- DELETE /products/<id>  - Delete a product

Orders:
- GET    /orders         - List all orders
- GET    /orders/<id>    - Retrieve an order
- POST   /orders         - Create an order
- DELETE /orders/<id>    - Delete an order

Testing the API

You can test the endpoints using:
- Postman (script for testing also added as "eighth commit")

Notes

- Each order must be associated with a user and one or more products.
- Product and order relations are many-to-many.
- All models are serialized with Marshmallow.
- App runs in debug mode by default - disable in production.