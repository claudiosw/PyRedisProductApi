from flask import Blueprint, jsonify, request
from src.main.adapters.request_adapter import request_adapter
from src.main.composer.product_finder_composer import product_finder_composer
from src.presentation.error_handler.error_controller import handle_errors
from src.validators.product_finder_validator import product_finder_validator

product_routes_bp = Blueprint("product_routes", __name__)


@product_routes_bp.route("/v1/products/<id>", methods=["GET"])
def get_product(id):
    http_response = None

    try:
        product_finder_validator(request)
        http_response = request_adapter(request, product_finder_composer().handle)
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
