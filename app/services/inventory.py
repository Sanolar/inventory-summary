from pathlib import Path
import csv
from datetime import datetime

SALES_FILE = Path(__file__).parent.parent / "db" / "sales.csv"

from app.api.db.csv_handler import load_inventory, save_inventory

LOW_STOCK_THRESHOLD = 5

def get_inventory():
    inventory = load_inventory()
    for item in inventory:
        item["low_stock"] = item["quantity"] < LOW_STOCK_THRESHOLD
    return inventory

def update_item(item_data):
    inventory = load_inventory()
    updated = False

    for item in inventory:
        if item["name"].lower() == item_data.name.lower():
            item["quantity"] = item_data.quantity
            item["price"] = item_data.price
            updated = True
            break

    if not updated:
        inventory.append({
            "name": item_data.name,
            "quantity": item_data.quantity,
            "price": item_data.price
        })

    save_inventory(inventory)
    return {"message": "Inventory updated", "item": item_data.dict()}


def record_sale(sale_items):
    inventory = load_inventory()
    total = 0
    errors = []
    summary = []

    for sold in sale_items:
        name = sold.name
        qty = sold.quantity
        for item in inventory:
            if item["name"].lower() == name.lower():
                if item["quantity"] < qty:
                    errors.append(f"Not enough stock for {name}")
                else:
                    item["quantity"] -= qty
                    total += qty * item["price"]
                    summary.append({
                        "name": name,
                        "quantity": qty,
                        "unit_price": item["price"],
                        "subtotal": qty * item["price"]
                    })
                break
        else:
            errors.append(f"{name} not found")

    save_inventory(inventory)
    return {
        "total": round(total, 2),
        "sold_items": summary,
        "errors": errors
    }
