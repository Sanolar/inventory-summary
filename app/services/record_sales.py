import csv
from datetime import datetime
from pathlib import Path
from app.api.db.csv_handler import load_inventory, save_inventory

# ✅ Define the sales.csv path before using it
SALES_FILE = Path(__file__).resolve().parent.parent / "db" / "sales.csv"

# 🐞 Optional debug print
print("DEBUG: Writing sales to:", SALES_FILE)

def record_sale(sale_data):
    inventory = load_inventory()
    total = 0
    items_sold = sale_data.items

    # Create the sales file with headers if it doesn't exist
    if not SALES_FILE.exists():
        with open(SALES_FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "product", "quantity_sold", "total_price"])

    with open(SALES_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        for sold_item in items_sold:
            name = sold_item.name
            quantity = sold_item.quantity

            for item in inventory:
                if item["name"].lower() == name.lower():
                    if item["quantity"] >= quantity:
                        item["quantity"] -= quantity
                        item_total = item["price"] * quantity
                        total += item_total

                        writer.writerow([
                            datetime.now().isoformat(),
                            name,
                            quantity,
                            item_total
                        ])
                        break
                    else:
                        raise ValueError(f"Not enough stock for {name}")

    save_inventory(inventory)
    return {"message": "Sale recorded", "total_sale": total}
