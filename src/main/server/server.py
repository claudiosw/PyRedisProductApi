from flask import Flask
from flask_cors import CORS
from src.infra.db.settings.connection import db_connection_handler
from src.infra.db.settings.cache_connection import cache_connection_handler
# Import Blueprints
from src.main.routes.product_routes import product_routes_bp


db_connection_handler.connect_to_db()
cache_connection_handler.connect_to_cache()
app = Flask(__name__)
CORS(app)


# Register Blueprints
app.register_blueprint(product_routes_bp)
