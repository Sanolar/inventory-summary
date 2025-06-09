from flask import Blueprint, request, jsonify
from app.services.inventory_service import (
    get_inventory, add_product, record_sale
)

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/", methods=["GET"])
def list_inventory():
    return jsonify(get_inventory())

@inventory_bp.route("/add", methods=["POST"])
def add():
    data = request.json
    result = add_product(data)
    return jsonify(result)

@inventory_bp.route("/sell", methods=["POST"])
def sell():
    data = request.json
    result = record_sale(data)
    return jsonify(result)
