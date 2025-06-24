import csv
from datetime import datetime
from pathlib import Path
from app.api.db.csv_handler import load_inventory, save_inventory
from app.schemas import SaleRequest

# ✅ Define the sales.csv path before using it
SALES_FILE = Path(__file__).resolve().parent.parent / "db" / "sales.csv"

# 🐞 Optional debug print
print("DEBUG: Writing sales to:", SALES_FILE)

def record_sale(sale_data: SaleRequest):
    inventory = load_inventory()
    total = 0
    receipt_items = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not SALES_FILE.exists():
        with open(SALES_FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "product", "quantity_sold", "total_price"])

    with open(SALES_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        for sold_item in sale_data.items:
            name = sold_item.name
            quantity = sold_item.quantity

            matched_item = next((item for item in inventory if item["name"].lower() == name.lower()), None)
            if not matched_item:
                receipt_items.append({
                    "name": name,
                    "quantity": quantity,
                    "status": "Not found"
                })
                continue

            if matched_item["quantity"] >= quantity:
                matched_item["quantity"] -= quantity
                item_total = matched_item["price"] * quantity
                total += item_total
                writer.writerow([timestamp, name, quantity, item_total])
                receipt_items.append({
                    "name": name,
                    "quantity": quantity,
                    "total": item_total,
                    "status": "Success"
                })
            else:
                receipt_items.append({
                    "name": name,
                    "quantity": quantity,
                    "status": "Out of stock. Check back later, thank you."
                })

    save_inventory(inventory)

    return {
        "message": "Sale processed",
        "timestamp": timestamp,
        "total_sale": total,
        "items": receipt_items,
        "note": "Thank you for your purchase."
    }
