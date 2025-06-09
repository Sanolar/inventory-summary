import csv, os
from datetime import datetime
from app.utils import INVENTORY_FILE, SALES_FILE, LOW_STOCK_THRESHOLD, ensure_files_exist

def get_inventory():
    ensure_files_exist()
    with open(INVENTORY_FILE, newline="") as f:
        rows = list(csv.DictReader(f))
        for row in rows:
            row["low_stock"] = int(row["qty"]) < LOW_STOCK_THRESHOLD
        return rows

def add_product(data):
    name, qty, price = data["name"], int(data["qty"]), float(data["price"])
    products = get_inventory()

    found = False
    for p in products:
        if p["name"].lower() == name.lower():
            p["qty"] = str(int(p["qty"]) + qty)
            p["price"] = str(price)
            found = True
            break
    if not found:
        products.append({"name": name, "qty": str(qty), "price": str(price)})

    with open(INVENTORY_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "qty", "price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)
    return {"message": f"{name} added/updated."}

def record_sale(data):
    items = data["items"]
    products = get_inventory()
    total_sale = 0
    sale_log = []

    for item in items:
        name, qty = item["name"], int(item["qty"])
        for p in products:
            if p["name"].lower() == name.lower():
                if int(p["qty"]) < qty:
                    return {"error": f"Not enough stock for {name}"}
                p["qty"] = str(int(p["qty"]) - qty)
                total = qty * float(p["price"])
                sale_log.append([datetime.now().isoformat(), name, qty, total])
                total_sale += total
                break
        else:
            return {"error": f"Product {name} not found"}

    with open(INVENTORY_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "qty", "price"])
        writer.writeheader()
        for p in products:
            p.pop("low_stock", None)  # Remove extra field before writing
            writer.writerow(p)

    with open(SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for log in sale_log:
            writer.writerow(log)

    return {"message": "Sale recorded", "total": total_sale}
